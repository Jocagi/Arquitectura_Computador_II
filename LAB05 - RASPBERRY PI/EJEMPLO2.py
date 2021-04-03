import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.IN)

while True:
    if GPIO.input(20):
        GPIO.output(21, False)
    else:
        GPIO.output(21, True)

