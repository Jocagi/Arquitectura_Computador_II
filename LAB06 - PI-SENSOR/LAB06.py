import RPi.GPIO as GPIO
import time
import datetime

sensor = 20
led = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

print("LAB06 - Jose Giron")

while True:
	if GPIO.input(sensor):
		GPIO.output(led, True)
		now = datetime.datetime.now()
		print("Interrupción en el sensor: " + now.strftime("%Y-%m-%d %H:%M:%S"))
		
		while GPIO.input(sensor):
			time.sleep(0.001)
	else:
		GPIO.output(led, False)

