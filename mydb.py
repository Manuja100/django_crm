import mysql.connector
from decouple import config

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = config('db_password') 
)

#prepare a cursor object
cursorObject = database.cursor()

#creating the db
cursorObject.execute("CREATE DATABASE crm_django")

print("Database Created!")