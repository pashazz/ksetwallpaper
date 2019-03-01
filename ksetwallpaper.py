#!/usr/bin/env python3
import dbus
import argparse

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

parser = argparse.ArgumentParser(description='KDE Wallpaper setter')
parser.add_argument('file', help='Wallpaper file name')
parser.add_argument('--plugin', '-p', help='Wallpaper plugin (default is org.kde.image)', default='org.kde.image')
args = parser.parse_args()


bus = dbus.SessionBus()
plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')

plasma.evaluateScript(jscript % (args.plugin, args.plugin, args.file))