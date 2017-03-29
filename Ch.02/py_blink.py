# py_blink.py - blinking built-in leds, using regular Python timing:

# This file was created on 29/03/2017
# Author: George Kaimakis

import time
import pyb

# define the leds:
green_led = 2
yellow_led = 3

while True:
    pyb.LED(green_led).on()
    pyb.LED(yellow_led).on()
    time.sleep(1)
    pyb.LED(green_led).off()
    pyb.LED(yellow_led).off()
    time.sleep(1)
