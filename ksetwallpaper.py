#!/usr/bin/env python3
import dbus
import argparse

jscript = """
var allDesktops = desktops();
print (allDesktops);
for (i=0;i<allDesktops.length;i++) {
    d = allDesktops[i];
    d.wallpaperPlugin = "org.kde.image";
    d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
    d.writeConfig("Image", "file://%s")
}
"""

parser = argparse.ArgumentParser(description='KDE Wallpaper setter')
parser.add_argument('file', help='Wallpaper file name')
args = parser.parse_args()


bus = dbus.SessionBus()
plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')

plasma.evaluateScript(jscript % args.file)