import mysql.connector
from mysql.connector import Error
from datetime import datetime
import sys
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "nooshin1385", "mysql")


def closing():
    if connection:
        connection.close()
    print("Connection closed.")

class user:
    def __init__(self, username , password):
        self.username = username
        self.password = password


