import os
import random
import string
from datetime import date
from io import BytesIO
import click
from PIL import Image
import requests


@click.command()
@click.option('--amount', '-a', default=100, help="How many pictures you want to find? By default, it's equal to 100.")
@click.option('--hash-length', '-l', default=0, help='How long the picture hash you want? For example, '
                                                     'https://i.imgur.com/123456.gif/, where 123456 is unique picture hash. '
                                                     'The length must be between 5 and 7. 5 is faster, but all pictures '
                                                     'are very old. 6 and 7 are slow, but pictures are newer. By default, '
                                                     "it's equal to random number between 5 and 7 for every picture.")
def main(amount, hash_length):
    """This little tool parses random pictures from https://imgur.com/ and
    saves it to [current working directory]\parsePic\[today's date]"""
    if hash_length > 7 or hash_length < 5 and hash_length != 0:
        raise SystemExit('The length must be between 5 and 7')
    count = 0
    path = f'{os.getcwd()}\\parsePic\\{date.today()}'
    if not os.path.exists(path):
        os.makedirs(path)
    while count < amount:
        hash = ''.join(random.choices(string.ascii_letters + string.digits, k=randomize_hash_length(hash_length)))
        link = requests.get(f'https://i.imgur.com/{hash}.gif')
        if link.url != 'https://i.imgur.com/removed.png' and link.headers['Content-Type'] == 'image/jpeg':
            count += 1
            print(count, link.url)
            image = Image.open(BytesIO(link.content))
            image.save(f'{path}\\{hash}.gif', 'GIF')


def randomize_hash_length(hash_length):
    if not hash_length:
        return random.randint(5, 7)
    return hash_length


if __name__ == '__main__':
    main()
