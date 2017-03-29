# blink_interrupt.py - demonstration of interrupt service routine:

# This file was created on 29/03/2017
# Author: George Kaimakis

import pyb

green_led   = 2
yellow_led  = 3

# interrupt service routine (ISR):
def BlinkYellow():
    pyb.LED(green_led).off()
    for x in range(0,4):
        pyb.LED(yellow_led).on()
        pyb.delay(250)
        pyb.LED(yellow_led).off()
        pyb.delay(250)

# create switch object and target ISR for 'callback':
sw = pyb.Switch()
sw.callback(BlinkYellow)

# infinite loop:
while True:
    pyb.LED(green_led).on()
    pyb.delay(1000)
    pyb.LED(green_led).off()
    pyb.delay(1000)
