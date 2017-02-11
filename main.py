#!/usr/bin/env python
from flask import Flask
from time import sleep
import RPi.GPIO as GPIO

def init():
    # Use RPi.GPIO layout (pin numbering)
    # GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # Setup pins
    print('Setup pins ... ')
    for gpio in [8, 10, 12, 16, 18, 22, 24, 26]:
        print('  -> pin %s as output' % gpio)
        GPIO.setup(gpio, GPIO.OUT)
        sleep(.1)
        # print('switch on pin %s' % gpio)
        GPIO.output(gpio, GPIO.LOW) # set switch on (relais are inverted)
        sleep(.1)
        # print('switch off pin %s' % gpio)
        GPIO.output(gpio, GPIO.HIGH) # set switch off (relais are inverted)
    print('done.')


app = Flask(__name__)

@app.route("/switch/<gpio>/<value>")
def switch(gpio, value):
    if value is 1:
        GPIO.output(gpio, GPIO.LOW)
    else:
        GPIO.output(gpio, GPIO.HIGH)

if __name__ == "__main__":
    init()
    app.run()
