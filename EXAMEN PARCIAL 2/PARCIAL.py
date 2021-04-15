import RPi.GPIO as GPIO
import time
import datetime
import mariadb 

#FUNCTION DEFINITION

def insertIntoDatabase(date, size, tiempo_agua, tiempo_shampoo, tiempo_rodillos, tiempo_escobas, tiempo_agua2, tiempo_secado):
        cur.execute("INSERT INTO PARCIAL (DATE, SIZE, TIEMPO_AGUA, TIEMPO_SHAMPOO, TIEMPO_RODILLOS, TIEMPO_ESCOBAS, TIEMPO_AGUA2, TIEMPO_SECADO) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (date, size, tiempo_agua, tiempo_shampoo, tiempo_rodillos, tiempo_escobas, tiempo_agua2, tiempo_secado))
        conn.commit()
        
def getCarSize(car_size):
        if(car_size == 1):
                return "PEQUEÑO"
        elif(car_size == 2):
                return "MEDIANO"
        else:
                return "GRANDE"
def getDate():
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        return date

#DATABSE CONNECTION
conn = mariadb.connect(
    user="a72520_jose167",
    password="XdJLB5U*x!-v.Pa",
    host="mysql5030.site4now.net",
    database="db_a72520_jose167")

cur = conn.cursor()

#GPIO CONFIGURATION
#Sensores
sensor1 = 5
sensor2 = 6
sensor3 = 13
#Luces
led_inicio = 20
led_fin = 21
led_agua = 17
led_shampoo = 27
led_rodillos = 22
led_escobas = 23
led_agua2 = 24
led_secado = 25

#GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_inicio, GPIO.OUT)
GPIO.setup(led_fin, GPIO.OUT)
GPIO.setup(led_agua, GPIO.OUT)
GPIO.setup(led_shampoo, GPIO.OUT)
GPIO.setup(led_rodillos, GPIO.OUT)
GPIO.setup(led_escobas, GPIO.OUT)
GPIO.setup(led_agua2, GPIO.OUT)
GPIO.setup(led_secado, GPIO.OUT)
GPIO.setup(sensor1, GPIO.IN)
GPIO.setup(sensor2, GPIO.IN)
GPIO.setup(sensor3, GPIO.IN)

#Tiempos
tiempo_inicio = 1
tiempo_fin = 1
tiempo_agua = 3
tiempo_shampoo = 1
tiempo_rodillos = 2
tiempo_escobas = 1
tiempo_agua2 = 1
tiempo_secado = 1

#PROGRAM

interruption = True

print("Parcial #2 - Jose Giron")

while True:
        #time
        now = datetime.datetime.now()
        start_date = now.strftime("%Y-%m-%d %H:%M:%S")
        #car attributes
        car_size = 1
		
        if (GPIO.input(sensor1) or GPIO.input(sensor2) or GPIO.input(sensor3)) and not(interruption):

                interruption = True

                #inicio de secuencia de lavado
                GPIO.output(led_inicio, True)
                print("Inicio de lavado en: " + start_date)

                #determinar tamaño del carro
                time.sleep(tiempo_inicio)
                if(GPIO.input(sensor2)):
                        car_size = 2
                if(GPIO.input(sensor3)):
                        car_size = 3
                string_carSize = getCarSize(car_size)
                print("Tamaño de carro: " + string_carSize)

                #Secuancia de lavado

                date = getDate()
                time.sleep(tiempo_agua)
                GPIO.output(led_agua, True)
                print("Activar agua: " + date)

                date = getDate()
                time.sleep(tiempo_shampoo)
                GPIO.output(led_shampoo, True)
                print("Activar shampoo: " + date)

                date = getDate()
                time.sleep(tiempo_rodillos)
                GPIO.output(led_rodillos, True)
                print("Activar rodillos: " + date)

                date = getDate()
                time.sleep(tiempo_escobas)
                GPIO.output(led_escobas, True)
                print("Activar escobas: " + date)

                date = getDate()
                time.sleep(tiempo_agua2)
                GPIO.output(led_agua2, True)
                print("Activar agua: " + date)

                date = getDate()
                time.sleep(tiempo_secado)
                GPIO.output(led_secado, True)
                print("Activar secado: " + date)

                #fin de secuencia
                time.sleep(tiempo_fin)
                GPIO.output(led_fin, True)
                print("Fin de lavado: " + date)

                #costo final
                costo = (tiempo_agua + tiempo_shampoo + tiempo_rodillos + tiempo_escobas + tiempo_agua2 + tiempo_secado) * 2 * car_size
                print("Costo final: Q." + str(costo))
                
                insertIntoDatabase(date, car_size, tiempo_agua, tiempo_shampoo, tiempo_rodillos, tiempo_escobas, tiempo_agua2, tiempo_secado)
        elif not(GPIO.input(sensor1) or GPIO.input(sensor2) or GPIO.input(sensor3)):
                time.sleep(1)
                #apagar leds
                GPIO.output(led_inicio, False)
                GPIO.output(led_fin, False)
                GPIO.output(led_agua, False)
                GPIO.output(led_shampoo, False)
                GPIO.output(led_rodillos, False)
                GPIO.output(led_escobas, False)
                GPIO.output(led_agua2, False)
                GPIO.output(led_secado, False)
                interruption = False
