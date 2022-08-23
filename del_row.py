import mysql.connector

mydb = mysql.connector.connect(
host = "localhost" , 
username = "system" , 
password = "8817", 
database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "delete from customer where name =%s"
val = ("ys",)
x  = input("do you want to delete data:")
if x  == 'y':
    mycursor.execute(sql,val)
    print("data deleted")

else:
    print("data still saved")


mydb.commit()

