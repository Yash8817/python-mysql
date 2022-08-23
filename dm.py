import mysql.connector

mydb  =  mysql.connector.connect(
    host  = "localhost " , 
    username  = "system"  , 
    password  = "8817" ,
    database = "mydatabase"
)

mycursor = mydb.cursor()

# sql = "create table student (id int auto_increment primary key , name varchar(10) , city varchar(10))"
# mycursor.execute(sql)

sql = "insert into student (name , city ) values (%s,%s)"
val = [
    ("sa" , "ahmedabad") , 
    ("rs" , "surat") , 
    ("bh" , "rajkot")  ,
    ("sw" , "thaltej")
   ]
mycursor.executemany(sql,val)



print("done")

