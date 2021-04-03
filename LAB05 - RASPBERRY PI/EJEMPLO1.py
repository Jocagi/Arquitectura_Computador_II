import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def blink(pin):
    GPIO.output(pin, True)
    time.sleep(1)
    GPIO.output(pin, False)
    time.sleep(1)
    return

for i in range(0, 50):
    blink(18)

GPIO.cleanup()
