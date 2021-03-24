### WARNING!

Using this tool, you can find (and you will) nude photos and other things that you might not want to see. I can't
promise that this will not happen, and I'm not responsible for this content.

### Usage:
`parsepic.exe [OPTIONS]`

This little tool parses random pictures from https://imgur.com/ and saves it to
_[current working directory]\\parsePic\\[today's date]_

Options:

  `-a, --amount INTEGER`       How many pictures you want to find? By default, it's equal to 100.

  `-l, --hash-length INTEGER`  How long the picture hash you want? For example, https://i.imgur.com/123456.gif/, 
  where 123456 is unique picture hash. The length must be between 5  and 7. 5 is faster, but all pictures are very old.
  6 and 7 are slow, but pictures are newer. By default, it's equal to random number between 5 and 7 for every picture.

  `--help`                     Show this message and exit.
