#!/usr/bin/env python

import psutil
import time
from collections import deque
import unicornhat as unicorn

print("""CPU Util Unicorn Hat

Displays CPU percentage usage in the Unicorn HAT or pHAT

If you're using a Unicorn HAT and only half the screen lights up,
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.4)
width,height=unicorn.get_shape()

"""matriz = deque([8, 4])
items.append(3) # deque == [1, 2, 3]
items.rotate(1) # The deque is now: [3, 1, 2]
items.rotate(-1) # Returns deque to original state: [1, 2, 3]
item = items.popleft() # deque == [2, 3]"""

matriz = [0, 0, 0, 0, 0, 0, 0]
columna = 0

while True:
    cpu =  psutil.cpu_percent(0.5)
    matriz.insert(0, int(cpu))
    matriz = matriz[0:7]
    columna = 0

    while (columna<8):
        for x in matriz:
            if x >= 0:
                y = 3
                r = 0
                g = 255
                b = 0
                unicorn.set_pixel(columna, y, r, g, b)
            if x >= 10:
                y = 3
                r = 56
                g = 255
                b = 0
                unicorn.set_pixel(columna, y, r, g, b)
            if  x >= 20:
                y = 3
                r = 113
                g = 255
                b = 0
                unicorn.set_pixel(columna, y, r, g, b)
            if  x >= 30:
                y = 2
                r = 170
                g = 255
                b = 0
                unicorn.set_pixel(columna, y, r, g, b)
            if x >= 40:
                y = 2
                r = 226
                g = 255
                b = 0
                unicorn.set_pixel(columna, y, r, g, b)
            if x >= 50:
                y = 2
                r = 255
                g = 226
                b = 0
                unicorn.set_pixel(columna, y, r, g, b)
            if  x >= 60:
                y = 1
                r = 255
                g = 170
                b = 0
                unicorn.set_pixel(columna, y, r, g, b)
            if  x >= 70:
                y = 1
                r = 186
                g = 113
                b = 0
                unicorn.set_pixel(columna, y, r, g, b)
            if x >= 80:
                y = 0
                r = 255
                g = 56
                b = 0
                unicorn.set_pixel(columna, y, r, g, b)
            if x >= 90:
                y = 0
                r = 255
                g = 0
                b = 0
                unicorn.set_pixel(columna, y, r, g, b)
            columna = columna + 1
    unicorn.show()
    unicorn.clear()
    print matriz
    time.sleep(0.5)
