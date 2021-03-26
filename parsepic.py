import os
import random
import string
from datetime import datetime
from io import BytesIO
import click
from PIL import Image
import requests
import dominate
from dominate.tags import img, style, p


@click.command()
@click.option('--amount', '-a', default=100,
              help="""How many pictures do you want to find? By default, it's equal to 100.""")
@click.option('--hash-length', '-l', default=0,
              help="""How long the picture hash do you want? For example, https://i.imgur.com/12345.gif/, where 12345
              is unique picture hash. The length must be between 5 and 7. 5 is faster, but all pictures are very old.
              6 and 7 are slow, but pictures are newer. By default, it's equal to random number between 5 and 7 for
              every picture.""")
@click.option('--save', '-s', default='html',
              help="""How do you want to save the pictures? All parameters save it to
              [current working directory]\\parsePic\\, but "html" saves it to  ...\\[today's date].html document,
              and "pic" saves it to ...\\[today's date] folder. By default, it's equal to "html".""")
def main(amount, hash_length, save):
    """This little tool parses random pictures from https://imgur.com/ and saves it to HTML-document or folder."""

    check_args(amount, hash_length, save)
    date = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    path = f'{os.getcwd()}\\parsePic\\'
    if html_save_method(save):
        page = prepare_page()
    else:
        path += date
    create_folders(path)
    count = 0
    while count < amount:
        hash = get_hash(hash_length)
        link = requests.get(f'https://i.imgur.com/{hash}.gif')
        if check_picture(link):
            count += 1
            print(count, link.url)
            if html_save_method(save):
                save_html(page, link, date)
            else:
                save_picture(path, link)


def check_args(amount, hash_length, save):
    if not isinstance(amount, int) or amount < 0:
        raise SystemExit('The amount must be a number greater then 0')
    if not isinstance(hash_length, int) or hash_length not in (0, 5, 6, 7):
        raise SystemExit('The length must be a number between 5 and 7')
    if not isinstance(save, str) or save not in ('html', 'pic'):
        raise SystemExit('The save must be "html" or "pic"')


def html_save_method(save):
    if save == 'html':
        return True
    return False


def prepare_page():
    page = dominate.document(title='parsePic')
    with page.head:
        style("""
            img {
                max-width: 1600px;
                max-height: 800px;
            }
        """)
    return page


def create_folders(path):
    if not os.path.exists(path):
        os.makedirs(path)


def get_hash(hash_length):
    if not hash_length:
        hash_length = random.randint(5, 7)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=hash_length))


def check_picture(link):
    if link.url != 'https://i.imgur.com/removed.png' and link.headers['Content-Type'] == 'image/jpeg':
        return True
    return False


def save_html(page, link, date):
    with page:
        p(img(src=f'{link.url}'))
    with open(f'parsePic\{date}.html', 'w') as html:
        html.write(page.render())


def save_picture(path, link):
    image = Image.open(BytesIO(link.content))
    image.save(f'{path}\\{hash}.gif', 'GIF')


if __name__ == '__main__':
    main()
