from io import RawIOBase
import mysql.connector

mydb = mysql.connector.connect(
host = "localhost" , 
username = "system" , 
password = "8817", 
database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customer limit 5 offset 2")
# start positoin
myresult = mycursor.fetchall()

for x in myresult:
       print(x)
