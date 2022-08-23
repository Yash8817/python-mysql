import mysql.connector
from mysql.connector.cursor import MySQLCursorDict
mydb  =  mysql.connector.connect(
    host  = "localhost " , 
    username  = "system"  , 
    password  = "8817" ,
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "create table student (id int auto_increment primary key, name varchar(10) , city varchar(10) , foreign key(id) references customer(id) )"
#sql  = "drop  table if exists student"
mycursor.execute(sql)
print("done")


mydb.commit()
mydb.close()