from os.path import join
import mysql.connector

mydb = mysql.connector.connect(
host = "localhost" , 
username = "system" , 
password = "8817", 
database = "mydatabase"
)

mycursor = mydb.cursor()
sql = ""

mycursor.execute(sql)


#result = 
for  x  in mycursor:
    print(x)
    

#mydb.commit()

