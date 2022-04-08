#!/usr/bin/env python3
import time
import dbus
import argparse
import glob
import random

def setwallpaper(filepath, plugin='org.kde.image'):
    jscript = """
    var allDesktops = desktops();
    print (allDesktops);
    for (i=0;i<allDesktops.length;i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = "%s";
        d.currentConfigGroup = Array("Wallpaper", "%s", "General");
        d.writeConfig("Image", "file://%s")
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object(
        'org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(jscript % (plugin, plugin, filepath))


def get_walls_from_folder(directory):
    # return  [f for f in listdir(folder) if isfile(join(folder, f))]
    return glob.glob(directory+'/*')


def wallpaper_slideshow(wallapapers, plugin, timer):
    if timer > 0:
        wallpaper_count = len(wallapapers)
        delta_s = timer
        s = int(delta_s % 60)
        m = int((delta_s / 60) % 60)
        h = int((delta_s / 3600) % 3600)
        if h > 0:
            timer_show = f"{h}h {m}m {s}s"
        elif m > 0:
            timer_show = f"{m}m {s}s"
        elif s > 0:
            timer_show = f"{s}s"
        print(
            f"Looping through {wallpaper_count} wallpapers every  {timer_show}")
        while True:
            random_int = random.randint(0, wallpaper_count-1)
            setwallpaper(wallapapers[random_int], plugin)
            time.sleep(timer)
    else:
        raise ValueError('Invalid --timer value')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='KDE Wallpaper setter')
    parser.add_argument('--file', help='Wallpaper file name', default=None)
    parser.add_argument(
        '--plugin', '-p', help='Wallpaper plugin (default is org.kde.image)', default='org.kde.image')
    parser.add_argument('--dir', '-d', type=str,
                        help='Absolute path of folder containging your wallpapers for slideshow', default=None)
    parser.add_argument('--timer', '-t', type=int,
                        help='Time in seconds between wallpapers', default=900)
    args = parser.parse_args()
    # setwallpaper(args.file, args.plugin)

    if args.file != None:
        setwallpaper(args.file, args.plugin)
    elif args.dir != None:
        wallpapers = get_walls_from_folder(args.dir)
        # print(wallpapers)
        wallpaper_slideshow(wallapapers=wallpapers,
                            plugin=args.plugin, timer=args.timer)
    else:
        print("Need help? use -h or --help")
