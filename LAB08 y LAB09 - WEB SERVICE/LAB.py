import RPi.GPIO as GPIO
import time
import datetime
import json
import urllib.request


#GPIO CONFIGURATION
#Sensores
sensor = 5
#Luces
display_A = 20
display_B = 21
display_C = 17
display_D = 27
display_E = 22
display_F = 23
display_G = 24
display_H = 25

#GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(display_A, GPIO.OUT)
GPIO.setup(display_B, GPIO.OUT)
GPIO.setup(display_C, GPIO.OUT)
GPIO.setup(display_D, GPIO.OUT)
GPIO.setup(display_E, GPIO.OUT)
GPIO.setup(display_F, GPIO.OUT)
GPIO.setup(display_G, GPIO.OUT)
GPIO.setup(display_H, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

interruption = True
url = "http://jose167-001-site1.dtempurl.com/"

print("LAB08/LAB09 - Jose Giron")

while True:
    if GPIO.input(sensor) and not(interruption):
        interruption = True

        #time
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        
        # download raw json object
        data = urllib.request.urlopen(url).read().decode()

        # parse json object
        obj = json.loads(data)

        # output some object attributes
        for value in obj:
            print("Interrupcion en: " + date)
            print(value["value"])
            #Output values
            #A
            segment_A = True if (value["value"][0]) == "1" else False
            GPIO.output(display_A, segment_A)
            #B
            segment_B = True if (value["value"][1]) == "1" else False
            GPIO.output(display_B, segment_B)
            #C
            segment_C = True if (value["value"][2]) == "1" else False
            GPIO.output(display_C, segment_C)
            #D
            segment_D = True if (value["value"][3]) == "1" else False
            GPIO.output(display_D, segment_D)
            #E
            segment_E = True if (value["value"][4]) == "1" else False
            GPIO.output(display_E, segment_E)
            #F
            segment_F = True if (value["value"][5]) == "1" else False
            GPIO.output(display_F, segment_F)
            #G
            segment_G = True if (value["value"][6]) == "1" else False
            GPIO.output(display_G, segment_G)
            #H
            segment_H = True if (value["value"][7]) == "1" else False
            GPIO.output(display_H, segment_H)
            
            
    elif not(GPIO.input(sensor)) and interruption:
        print("No value")
        interruption = False
