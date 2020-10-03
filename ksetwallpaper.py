!/usr/bin/env python3
import dbus
import argparse
import os
#from os import listdir
#from os.path import expanduser
#import random


def setwallpapers(filepath, plugin = 'org.kde.image'):
    # I'm not sure how to get a list of desktops, this function should iterate over a list and call setwallpaper
    jscript = """
    var allDesktops = desktops();
    for (i=0;i<allDesktops.length;i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = "%s";
        d.currentConfigGroup = Array("Wallpaper", "%s", "General");
        d.writeConfig("Image", "file://%s")
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(jscript % (plugin, plugin, filepath))


def setwallpaper(desktop, filepath, plugin = 'org.kde.image'):
    jscript = """
    i = %s
    d = desktops()[i];
    d.wallpaperPlugin = "%s";
    d.currentConfigGroup = Array("Wallpaper", "%s", "General");
    d.writeConfig("Image", "file://%s")
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(jscript % (desktop, plugin, plugin, filepath))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='KDE Wallpaper setter')
    parser.add_argument('file', help='Wallpaper file name')
    parser.add_argument('--plugin', '-p', help='Wallpaper plugin (default is org.kde.image)', default='org.kde.image')
    args = parser.parse_args()
    #image_path = expanduser("~") + "/Pictures/Spotlight/"
    #images = listdir(image_path)
    #del images[images.index(os.path.basename(args.file))]
    #random_image = random.choice(images)
    # if more than one desktop?
    # setwallpapers(args.file, args.plugin)
    # 0 is the first desktop
    setwallpaper(0, args.file, args.plugin)
    # 2 is apparently second
    # setwallpaper(2, image_path + random_image, args.plugin)
