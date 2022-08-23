import mysql.connector

mydb =  mysql.connector.connect(
host ="localhost " , 
username = "system"  ,
password  = "8817" , 
database  = "mydatabase"
)

mycursor  = mydb.cursor()

sql = "describe customer" 

mycursor.execute(sql)

for  x  in mycursor:
    print(x)

