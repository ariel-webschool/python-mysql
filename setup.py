import mysql.connector

db_name="webschool_test"
table_name="users"

def create_table():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=db_name
  )
  mycursor = mydb.cursor()
  mycursor.execute(f"CREATE TABLE {table_name} (name VARCHAR(255), password VARCHAR(255))")

def create_database():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
  )
  mycursor = mydb.cursor()
  mycursor.execute(f"CREATE DATABASE {db_name}")

def seed_database():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=db_name
  )
  mycursor = mydb.cursor()
  sql = f"INSERT INTO {table_name} (name, password) VALUES (%s, %s)"
  val = [("Jordan", "jordan5"),("Zeev", "zeev12345"),("Ariel","345566"),("Itshak","I437879821"),("Jessy","Jessy78797698")]
  mycursor.executemany(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")

def rollback():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
  )
  mycursor = mydb.cursor()
  mycursor.execute(f"DROP DATABASE {db_name}")

rollback()
create_database()
create_table()
seed_database()