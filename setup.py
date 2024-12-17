import mysql.connector
from mysql.connector import Error

# Constants for database and table names
db_name = "webschool_test"
table_name = "users"

def get_database_connection(database=None):
    """Creates a database connection."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=database
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_database():
    """Creates the database if it does not already exist."""
    connection = get_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"Database '{db_name}' created or already exists.")
        except Error as e:
            print(f"SQL Error: {e}")
        finally:
            cursor.close()
            connection.close()

def create_table():
    """Creates the table in the specified database."""
    connection = get_database_connection(database=db_name)
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """)
            print(f"Table '{table_name}' created or already exists.")
        except Error as e:
            print(f"SQL Error: {e}")
        finally:
            cursor.close()
            connection.close()

def seed_database():
    """Inserts initial data into the table."""
    connection = get_database_connection(database=db_name)
    if connection:
        try:
            cursor = connection.cursor()
            sql = f"INSERT INTO {table_name} (name, password) VALUES (%s, %s)"
            val = [
                ("Jordan", "jordan5"),
                ("Zeev", "zeev12345"),
                ("Ariel", "345566"),
                ("Itshak", "I437879821"),
                ("Jessy", "Jessy78797698")
            ]
            cursor.executemany(sql, val)
            connection.commit()
            print(f"{cursor.rowcount} records inserted into '{table_name}'.")
        except Error as e:
            print(f"SQL Error: {e}")
        finally:
            cursor.close()
            connection.close()

def rollback():
    """Deletes the database to reset the environment."""
    connection = get_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"DROP DATABASE IF EXISTS `{db_name}`")
            print(f"Database '{db_name}' dropped.")
        except Error as e:
            print(f"SQL Error: {e}")
        finally:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    rollback()  # Optional: Clear the database before starting
    create_database()
    create_table()
    seed_database()
