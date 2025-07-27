#!/usr/bin/python

from openrazer.client import DeviceManager as dm

dev = next(
    (d for d in dm().devices if d.name == "Razer Viper Ultimate (Wireless)"),
    None
)

if dev == None:
    print('device not found')
    exit()

print(f"Battery: {dev.battery_level}% ({dev.is_charging and '+' or '-'})")
