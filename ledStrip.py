import neopixel
import machine
import time

ledStrip = neopixel.NeoPixel(machine.Pin(5), 28, bpp=3, timing=1)
colors = [(255, 255, 255), (0, 0, 0)]

def colorWipe(strip, color, wait_ms=50):
    for i in range(28):
        strip.__setitem__(i, color)
        strip.write()
        time.sleep(wait_ms / 1000.0)

while True:
    for i in range (2):
        colorWipe(ledStrip, colors[i])
