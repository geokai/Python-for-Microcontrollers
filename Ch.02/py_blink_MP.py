# py_blink_MP.py - blinking built-in leds, using MicroPython timing:

# This file was created on 29/03/2017
# Author: George Kaimakis

import pyb

# define the leds:
green_led   = 2
yellow_led  = 3

while True:
    pyb.LED(green_led).on()
    pyb.LED(yellow_led).on()
    # the delay method in pyb uses milliseconds for units of delay:
    pyb.delay(1000)
    pyb.LED(green_led).off()
    pyb.LED(yellow_led).off()
    pyb.delay(1000)
