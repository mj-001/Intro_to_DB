import mysql.connector
from mysql.connector import errorcode


def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="john_njogo",
            password="ALX_MYSQL"
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        connection.commit()

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username or password.")
        else:
            print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


if __name__ == "__main__":
    create_database()
