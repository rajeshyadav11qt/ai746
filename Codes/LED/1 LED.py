import RPI.GPIO as GPIO 
import time

GPIO.setmode (GPIO.BOARD)

GPIO.setup(11,GPIO.OUT) 

While True: 
GPIO.output(11,True)
time.sleep(1)
GPIO.output(11,False)
time.sleep(1)
