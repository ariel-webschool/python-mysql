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

sql = f"INSERT INTO {table_name} (name, password) VALUES (%s, %s)"
val = [("Zeev", "zeev12345"),("Ariel","345566"),("Jessy","Jessy78797698")]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")