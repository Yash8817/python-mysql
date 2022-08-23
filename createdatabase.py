import mysql.connector

mydb =  mysql.connector.connect(
host  = "localhost", 
username  = "system", 
password = "8817"
)

if mydb.is_connected :
    print("connected")

else:
    print("not connected")



mycursor =  mydb.cursor()

#mycursor.execute("create database mydatabase")
# check database is created or not 
mycursor.execute("show databases")
# list all database 
for x  in mycursor:
    print(x)


mydb.close()
print("database closed")