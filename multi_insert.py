import mysql.connector
from mysql.connector.cursor import MySQLCursorBufferedDict

mydb  = mysql.connector.connect(
host  = "localhost" , 
username = "system" , 
password   = "8817" , 
database   = "mydatabase"
)

mycursor   =  mydb.cursor()
 
sql = "insert into student (name , city ) values (%s,%s)"
val = [
    ("hs" , "ahmedabad") , 
    ("rq" , "surat") , 
    ("rr" , "rajkot")  ,
    ("hj" , "thaltej") , 
    ("lj" , "baroda")

   ]

mycursor.executemany(sql , val)


sql =  "SELECT * FROM student"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)



mydb.commit()
print("after commit")



