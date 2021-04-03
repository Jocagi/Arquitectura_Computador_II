#!/usr/bin/python 
import mariadb 

conn = mariadb.connect(
    user="root",
    password="raspberry",
    host="localhost",
    database="exampledb")

cur = conn.cursor() 

#retrieving information 
print("### Consultando informacion ###")
some_name = "Jose" 
cur.execute("SELECT ID,name FROM dataTable WHERE name=?", (some_name,)) 

for ID, name in cur: 
	print(f"ID: {ID}, Name: {name}")
    
#insert information 
print("### Insertando datos ###")
try: 
	cur.execute("INSERT INTO dataTable (ID, name) VALUES (?, ?)", (8,"TestName")) 
except mariadb.Error as e: 
	print(f"Error: {e}")

conn.commit() 
print(f"Last Inserted ID: {cur.lastrowid}")

#Select All
print("### Tabla completa ###")
cur.execute("SELECT * FROM dataTable;") 

for ID, name in cur: 
	print(f"ID: {ID}, Name: {name}")
    
conn.close()