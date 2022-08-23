import mysql.connector

mydb = mysql.connector.connect(
host   = "localhost" , 
username = "system" , 
password = "8817" , 
database  = "mydatabase"
) 
mycursor  = mydb.cursor()

sql  = "INSERT INTO customer (name , city ) values (%s,%s)"
val = ("yash","ahmedabad")
mycursor.execute(sql,val)
print("data interted")

print("last row id is :" , mycursor.lastrowid)



mydb.close()