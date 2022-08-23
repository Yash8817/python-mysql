from io import RawIOBase
import mysql.connector

mydb = mysql.connector.connect(
host = "localhost" , 
username = "system" , 
password = "8817", 
database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customer")

myresult = mycursor.fetchall()

for x in myresult:
       print(x)




print("")
print("city =\'ahmedabad\'")
mycursor = mydb.cursor()
sql = "SELECT * FROM customer WHERE city ='ahmedabad'"
mycursor.execute(sql)
result  = mycursor.fetchall()
for x in result:
    print(x)



print("")
print("only one row")
sql = "select * from customer where name =%s"
val = ("vk",)
mycursor.execute(sql , val)
myresult = mycursor.fetchall()
print(myresult)
mydb.commit()
