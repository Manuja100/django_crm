import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '21323966' 
)

#prepare a cursor object
cursorObject = database.cursor()

#creating the db
cursorObject.execute("CREATE DATABASE crm_django")

print("Database Created ")