import RPi.GPIO as GPIO
import time
import datetime
import mariadb 

#FUNCTION DEFINITION

def insertIntoDatabase(date, activity):
        cur.execute("INSERT INTO LAB07 (DATE, ACTIVITY) VALUES (?, ?)", (date, activity))
        conn.commit()

#DATABSE CONNECTION
conn = mariadb.connect(
    user="a72520_jose167",
    password="XdJLB5U*x!-v.Pa",
    host="mysql5030.site4now.net",
    database="db_a72520_jose167")

cur = conn.cursor()

#GPIO CONFIGURATION
sensor = 20
led = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

#PROGRAM

interruption = True

print("LAB07 - Jose Giron")

while True:
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
		
        if GPIO.input(sensor) and not(interruption):
                interruption = True
                GPIO.output(led, True)
                activity = "INTERRUPCION"
                print("Interrupción en el sensor: " + date)
                insertIntoDatabase(date, activity)
        elif not(GPIO.input(sensor)) and interruption:
                interruption = False
                GPIO.output(led, False)
                activity = "CONTINUIDAD"
                print("Continuidad en el sensor: " + date)
                insertIntoDatabase(date, activity)
