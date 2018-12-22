#!/usr/bin/python3

# Run PNG file in loop, row by row, on the 28 LEDs of a LED SHIM from @Pimoroni
# This is a quick hack, it is not bullet proof.

# Copyright David Glaude 2018

import png
import time
import ledshim
import sys

ledshim.set_clear_on_exit()

filename = sys.argv[1]
r=png.Reader(filename)
r.asRGB8() # Forced 8 bit RGB (fail if Alpha is present)
t=r.read()

ll = list(t[2]) # Pixels data in boxed row flat pixel format

line_number=0

while(True):
    line=ll[line_number] # Take one line
    i=0
    pixel=0
    if t[0] == 1:
        r, g, b = line
        ledshim.set_all(r, g, b)
    else:
        for value in line:
            if pixel < ledshim.NUM_PIXELS:
                if i%3 == 0:
                    r = value
                if i%3 == 1:
                    g = value
                if i%3 == 2:
                    b = value
                    ledshim.set_pixel(pixel, r, g, b)
                    pixel = pixel + 1
            i = i + 1
    ledshim.show()
    time.sleep(0.001) 
    line_number = line_number + 1
    if line_number == t[1]:
        line_number = 0

