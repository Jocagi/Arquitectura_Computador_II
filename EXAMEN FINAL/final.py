import RPi.GPIO as GPIO
import time
from time import sleep
import datetime

#Definitios
morse_low = 0.1
morse_high = 0.8
morse_off = 0.5

#GPIO CONFIGURATION
#Display
display_A = 20
display_B = 21
display_C = 17
display_D = 27
display_E = 22
display_F = 23
display_G = 24
display_H = 25
morse = 26

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
GPIO.setup(morse, GPIO.OUT)

def _MorseValue(number):
    if(number == 0):
        return '-----'
    elif(number == 1):
        return '.----'
    elif(number == 2):
        return '..---'
    elif(number == 3):
        return '...--'
    elif(number == 4):
        return '....-'
    elif(number == 5):
        return '.....'
    elif(number == 6):
        return '-....'
    elif(number == 7):
        return '--...'
    elif(number == 8):
        return '---..'
    elif(number == 9):
        return '----.'
    else:
        return '11111100'

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

def MorseDisplay(number):
    value = _MorseValue(number)
    GPIO.output(morse, False)
    sleep(1)
    #Output values
    for i in value:
        GPIO.output(morse, True)
        if (i == "."):
            time.sleep(morse_low)
        else:
            time.sleep(morse_high)
        GPIO.output(morse, False)
        time.sleep(morse_off)

def runApp():
    while(True):
        #Instrucciones
        print("Introduzca la secuencia a enviar:")
        #Valores recibidos
        value = str(input())
        #Validar que entrada son numeros
        try:
            val = int(value)
            #Validar un máximo de 10 digitos
            if(len(str(value)) <= 10):
                for number in value:
                    _7SegmentDisplay(int(number))
                    MorseDisplay(int(number))
            else:
                print("El máximo son 10 digitos")
        except ValueError:
            print("La entrada deben ser solo numeros")

if __name__ == '__main__':
    print("Program started")
    runApp()
