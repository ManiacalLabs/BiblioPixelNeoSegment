from bibliopixel.drivers.serial import Serial
from bibliopixel import colors
import time
import collections
from NeoSegment import NeoSegment
from NeoSegment.demo_anims import RGBClock, ScrollText
from bibliopixel import log

rainbow = [
    colors.Red,
    colors.Orange,
    colors.Yellow,
    colors.Green,
    colors.Blue,
    colors.Indigo,
    colors.Violet
]

driver = Serial(num=49, ledtype='NEOPIXEL', c_order='GRB')
layout = NeoSegment(driver, brightness=128)

# Generate string of all valid characters for NeoSegment
msg = ''
for i in range(32, 123, 1):
    msg += chr(i)
msg += '      '

while True:
    anim = RGBClock(layout)
    anim.run(fps=2, seconds=8)

    anim = ScrollText(layout, msg, rainbow)
    anim.run(fps=5, until_complete=True)

    anim = ScrollText(layout, "NEOSEGMENT IS COOL", rainbow)
    anim.run(fps=5, until_complete=True)
