from logging import disable
import mysql.connector
from mysql.connector.connection import MySQLConnection 


mydb =   mysql.connector.connect(
host="localhost" , 
username= "system" , 
password = "8817"
)

print(mydb)
mydb.close()





