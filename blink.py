#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
print "Raspberry Pi v" + `GPIO.RPI_REVISION`

print "Setup Pin"
GPIO.setup(22, GPIO.OUT)

var=1
print "Start Loop"
while var == 1:
    print "LED OFF"
    GPIO.output(22, False)
    time.sleep(1)
    print "LED ON"
    GPIO.output(22, True)
    time.sleep(1)

