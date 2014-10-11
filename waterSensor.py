#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import signal
import sys

def sig_handler(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)

GPIO.setmode(GPIO.BOARD)

print "Setup Pin"
GPIO.setup(32, GPIO.IN)
GPIO.setup(22, GPIO.OUT)

def waterCheck(channel):
    state = GPIO.input(32)
    if (state == 0 ):
        GPIO.output(22, True)
        print "Water Detected."
    else:
        GPIO.output(22, False)
        print "No Water"


GPIO.add_event_detect(32, GPIO.BOTH, callback=waterCheck)

while True:
    time.sleep(1)

