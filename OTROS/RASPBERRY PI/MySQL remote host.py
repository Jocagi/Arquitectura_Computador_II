#!/usr/bin/python 
import mariadb 

conn = mariadb.connect(
    user="a72520_jose167",
    password="XdJLB5U*x!-v.Pa",
    host="mysql5030.site4now.net",
    database="db_a72520_jose167")

cur = conn.cursor()
#cur.execute("CREATE TABLE TEST (ID INT, NAME NVARCHAR(50))")
#conn.commit()

cur.execute("INSERT INTO TEST (ID, name) VALUES (3, 'Jose')")
cur.execute("INSERT INTO TEST (ID, name) VALUES (4, 'Karen')")
conn.commit()

cur.execute("SELECT * FROM TEST;") 

for ID, name in cur: 
	print(f"ID: {ID}, Name: {name}")
    
conn.close() 
