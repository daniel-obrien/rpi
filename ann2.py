#simple GPIO running on RPI Python code

import RPi.GPIO as GPIO  #GPIO's are General Purpose Inputs and Outputs. The pins.

GPIO.setmode(GPIO.BOARD)

GPIO.setup(4,GPIO.OUT) #sets pin 4 up
GPIO.setup(14,GPIO.OUT) #sets pin 14 up

GPIO.output(4, GPIO.HIGH) #runs pin 4 at high
GPIO.output(14, GPIO.HIGH) #runs pin 4 at high






#add extra python code here!!!!

