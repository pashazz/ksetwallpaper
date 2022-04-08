# KDE set wallpaper script
## Usage
```sh
-h, --help
                    show this help message and exit
file FILE
                    Wallpaper file name
--plugin PLUGIN, -p PLUGIN
                    Wallpaper plugin (default is org.kde.image)
--dir DIR, -d DIR
                    Absolute path of folder containging your wallpapers for slideshow
--timer TIMER, -t TIMER
                    Time in seconds between wallpapers
```
 - Set one wallpaper on all monitors

`python3 ksetwallpaper.py filename`

 - Start random slideshow from images folder with updating time of 30 minutes

`python3 ksetwallpaper.py -d ' /folder/with/Wallpapers' -p org.kde.image -t 1800`

## Bugs
Plasma does not update the image of the same file name when it is replaced

## [wallpaper-reddit](https://github.com/markubiak/wallpaper-reddit) integration:
#### This assumes that you've copied ksetwallpaper.py to your $PATH and chmod +x'd it

Apply this [patch](https://gist.github.com/pashazz/84846bad449910c684245e5c141d8a3c) to wallpaper.py
(located in `/usr/lib/python3.6/site-packages/wpreddit/`)

## License
GPL v3
