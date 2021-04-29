from flask import Flask, request
from multiprocessing import Process
import os
import RPi.GPIO as GPIO
import time
from time import sleep
import datetime
import requests

#GPIO CONFIGURATION
#Entrada
bit_0 = 5
bit_1 = 6
bit_2 = 13
bit_3 = 19
#Display
display_A = 20
display_B = 21
display_C = 17
display_D = 27
display_E = 22
display_F = 23
display_G = 24
display_H = 25
out_1 = 26
foco = 12
send = 18

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
GPIO.setup(out_1, GPIO.OUT)
GPIO.setup(foco, GPIO.OUT)
GPIO.setup(bit_0, GPIO.IN)
GPIO.setup(bit_1, GPIO.IN)
GPIO.setup(bit_2, GPIO.IN)
GPIO.setup(bit_3, GPIO.IN)
GPIO.setup(send, GPIO.IN)

app = Flask(__name__)


def _7SegmentValue(number):
    if(number == 0):
        return '11111100'
    elif(number == 1):
        return '01100000'
    elif(number == 2):
        return '11011010'
    elif(number == 3):
        return '11110010'
    elif(number == 4):
        return '01100110'
    elif(number == 5):
        return '10110110'
    elif(number == 6):
        return '10111110'
    elif(number == 7):
        return '11100000'
    elif(number == 8):
        return '11111110'
    elif(number == 9):
        return '11110110'
    else:
        return '11111100'

def _7SegmentDisplay(number):
    carry = number / 10
    module = number % 10
    value = _7SegmentValue(module)
    #Output values
    #A
    segment_A = True if (value[0]) == "1" else False
    GPIO.output(display_A, segment_A)
    #B
    segment_B = True if (value[1]) == "1" else False
    GPIO.output(display_B, segment_B)
    #C
    segment_C = True if (value[2]) == "1" else False
    GPIO.output(display_C, segment_C)
    #D
    segment_D = True if (value[3]) == "1" else False
    GPIO.output(display_D, segment_D)
    #E
    segment_E = True if (value[4]) == "1" else False
    GPIO.output(display_E, segment_E)
    #F
    segment_F = True if (value[5]) == "1" else False
    GPIO.output(display_F, segment_F)
    #G
    segment_G = True if (value[6]) == "1" else False
    GPIO.output(display_G, segment_G)
    #H
    segment_H = True if (value[7]) == "1" else False
    GPIO.output(display_H, segment_H)
    #Salidas adicionales
    #Mayor a 10
    led = True if (carry >= 1) else False
    GPIO.output(out_1, led)
    #Foco
    for i in range(number):
        sleep(1)
        GPIO.output(foco, True)
        sleep(1)
        GPIO.output(foco, False)

@app.route('/')
def index():
    return "Hello World"

@app.route("/<data>")
def action(data):
    result = "Resultado:" + str(data)
    _7SegmentDisplay(int(data))
    print(result)
    return (result)

def runWebServer():
    print("Web Server Started")
    app.run(debug=True, port=80, host='0.0.0.0')

def runApp():
    print("Main program started")
    while(True):
        #time
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        #input
        binary = "0"
        if GPIO.input(send):
            bit0 = "1" if (GPIO.input(bit_0)) else "0"
            bit1 = "1" if (GPIO.input(bit_1)) else "0"
            bit2 = "1" if (GPIO.input(bit_2)) else "0"
            bit3 = "1" if (GPIO.input(bit_3)) else "0"
            binary = bit3 + bit2 + bit1 + bit0
            print("Value:" + binary)
            #Web request
            url = 'http://192.168.242.12/' + date + '/' + str(binary)
            x = requests.get(url)
            print("Web response:" + str(x.text))
            sleep(1)

if __name__ == '__main__':
    print("Program started")
    p = Process(target=runWebServer)
    p.start()
    sleep(1)
    runApp()
