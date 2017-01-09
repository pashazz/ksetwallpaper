# KDE set wallpaper script
## Usage

`python3 ksetwallpaper.py filename`

## Bugs
Plasma does not update the image of the same file name when it is replaced

## [wallpaper-reddit](https://github.com/markubiak/wallpaper-reddit) integration:
#### This assumes that you've copied ksetwallpaper.py to your $PATH and chmod +x'd it

Apply this [patch](https://gist.github.com/pashazz/84846bad449910c684245e5c141d8a3c) to wallpaper.py
(located in `/usr/lib/python3.6/site-packages/wpreddit/`)

## License
GPL v3
