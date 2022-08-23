import mysql.connector


mydb  = mysql.connector.connect(
host  = "localhost ",
username = "system" , 
password = "8817" , 
database  = "mydatabase " , 
)


if mydb.is_connected :
    print("connected")


x  = input("1 to close")
if x == 1:
    print("disconnected")
    mydb.close()


mydb.is_closed() 
print("closed")

