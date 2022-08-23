import mysql.connector

mydb = mysql.connector.connect(
host = "localhost" , 
username = "system" , 
password = "8817", 
database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "select * from customer order by  name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(myresult)
mydb.commit()
