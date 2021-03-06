import RPi.GPIO as GPIO
import time
import datetime

#GPIO CONFIGURATION
sensor = 20
led = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

#PROGRAM

interruption = True

print("LAB06 - Jose Giron")

while True:
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
		
        if GPIO.input(sensor) and not(interruption):
                interruption = True
                GPIO.output(led, True)
                print("Interrupción en el sensor: " + date)
        elif not(GPIO.input(sensor)) and interruption:
                interruption = False
                GPIO.output(led, False)
                print("Continuidad en el sensor: " + date)
