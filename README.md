### WARNING!

Using this tool, you can find (and you will) nude photos and other things that you might not want to see. I can't
promise that this will not happen, and I'm not responsible for this content.

### Usage:
`parsepic.exe [OPTIONS]`

  This little tool parses random pictures from https://imgur.com/ and saves it to HTML-document or folder.

Options:

  `-a, --amount INTEGER`       How many pictures do you want to find? By default, it's equal to 100.

  `-l, --hash-length INTEGER`  How long the picture hash do you want? For example, https://i.imgur.com/12345.gif/,
  where 12345 is unique picture hash. The length must be between 5 and 7. 5 is faster, but all pictures are very old.
  6 and 7 are slow, but pictures are newer. By default, it's equal to random number between 5 and 7 for
  every picture.

  `-s, --save TEXT`            How do you want to save the pictures? All parameters save it to _[current working
  directory]\parsePic\_, but "html" saves it to _...\[today's date].html document_, and "pic" saves it to
  _...\[today's date] folder_. By default, it's equal to "html".


  `--help`                     Show this message and exit.
