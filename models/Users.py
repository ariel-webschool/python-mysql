import mysql.connector

class Users:
	
	def __init__(self):
		print("User")

	def delete(self, name):
		db_name="webschool_test"
		table_name="users"
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database=db_name
		)
		mycursor = mydb.cursor()
		sql = f"DELETE FROM {table_name} WHERE name='{name}'"
		mycursor.execute(sql)
		mydb.commit()
		print(mycursor.rowcount, "record deleted.")
	
	def update(self, user):
		print(user)
		db_name="webschool_test"
		table_name="users"
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database=db_name
		)
		mycursor = mydb.cursor()
		sql = f"UPDATE {table_name} SET password='{user["password"]}' WHERE name='{user["name"]}'"
		mycursor.execute(sql)
		mydb.commit()
		print(mycursor.rowcount, "record update.")
  
	def all(self):
		db_name="webschool_test"
		table_name="users"
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database=db_name
		)
		mycursor = mydb.cursor()
		sql = f"SELECT * FROM {table_name}"
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		return myresult
    
	def find(self,name):
		db_name="webschool_test"
		table_name="users"
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database=db_name
		)
		mycursor = mydb.cursor()
		sql = f"SELECT * FROM {table_name} WHERE name='{name}'"
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		for x in myresult:
			print(x)
    
	def add(self, name, password):
		db_name="webschool_test"
		table_name="users"
  
		connection = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database=db_name,
       		charset="utf8mb4"
		)
		cursor = connection.cursor()
		sql = f"INSERT INTO `{table_name}` (name, password) VALUES (%s, %s)"
		val = (name, password)
		cursor.execute(sql, val)
		connection.commit()
		cursor.close()
		connection.close()
		print(cursor.rowcount, "record inserted.")