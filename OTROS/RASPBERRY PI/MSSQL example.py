import pyodbc 
# Use connection string to database 
server = 'sql5103.site4now.net' 
database = 'DB_A72520_jose167' 
username = 'DB_A72520_jose167_admin' 
password = 'XdJLB5U*x!-v.Pa' 
conn = pyodbc.connect('DRIVER={FreeTDS};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

cursor.execute('SELECT * FROM dbo.TEST')

for row in cursor:
    print(row)
