import mysql.connector
from mysql.connector import errorcode

def connect_to_mysql_server():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="john_njogo",
            password="ALX_MYSQL"
        )
        print("Connection to MySQL server successful.")
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username or password.")
        else:
            print(f"Error: {err}")
        return None


def create_database(connection):
    try:
        cursor = connection.cursor()
        db_name = "alx_book_store"
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        connection.commit()
        print(f"Database '{db_name}' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: Could not create database. {err}")
    finally:
        cursor.close()


def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")



def main():
    connection = connect_to_mysql_server()
    if connection:
        create_database(connection)
        close_connection(connection)



if __name__ == "__main__":
    main()
