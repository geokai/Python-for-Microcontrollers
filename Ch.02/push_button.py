# push_button.py - pressing the pushbutton lights up the led:

# This file was created on 29/03/2017
# Author: George Kaimakis

from pyb import Pin

# create pin objects:
pinX1 = Pin('X1', Pin.IN, Pin.PULL_UP)
pinX2 = Pin('X2', Pin.OUT_PP)

while True:
    if pinX1.value() == 0:
        pinX2.high()
    else:
        pinX2.low()
