import mysql.connector

mydb  =  mysql.connector.connect(
host  ="localhost" , 
username = "system" , 
password  ="8817" , 
database  = "mydatabase"
)
 

mycursor  = mydb.cursor()

mycursor.execute("create table customer (id int auto_increment primary key  ,  name varchar(20)  ,  city varchar(10))")
# to add primary key in existing table
# (alter table customer add column id int auto_crement ,name varchar(20))
mycursor.execute("show tables") 
for x  in mycursor:
    print(x)

mydb.close()
