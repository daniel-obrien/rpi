#simple GPIO running on RPI Python code

import RPi.GPIO as GPIO  #GPIO's are General Purpose Inputs and Outputs. The pins.
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.OUT) #sets pin 23 up
GPIO.setup(24,GPIO.OUT) #sets pin 24 up

GPIO.setup(27,GPIO.OUT) #sets pin 27 up
GPIO.setup(22,GPIO.OUT) #sets pin 22 up

GPIO.output(27, GPIO.HIGH) #runs pin 4 at high
GPIO.output(22, GPIO.LOW) #runs pin 4 at high
GPIO.output(23, GPIO.HIGH) #runs pin 4 at high
GPIO.output(24, GPIO.LOW) #runs pin 4 at high

sleep(3)

GPIO.cleanup()        #stops all signals to pins


#add extra python code here!!!!

