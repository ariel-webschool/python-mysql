import mysql.connector

db_name="webschool_test"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute(f"CREATE DATABASE {db_name}")