import mysql.connector
db_name="webschool_test"
table_name="users"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database=db_name
)

mycursor = mydb.cursor()

mycursor.execute(f"CREATE TABLE {table_name} (name VARCHAR(255), password VARCHAR(255))")