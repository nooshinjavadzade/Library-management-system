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

class member:
    def __init__(self, firstname , lastname , username , password , email ):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        join_date = datetime.now().strftime('%Y-%m-%d')

    def if_join(self, username):
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM members WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        cursor.close()

        if result[0] > 0:
            return True
        else:
            return False

    def add_user(self):
        if not self.if_join():
            cursor = connection.cursor()
            query = "INSERT INTO members (firstname, lastname, username, password, join_date , email) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (self.firstname, self.lastname, self.age, self.username, self.password, self.join_date , self.email)
            try:
                cursor.execute(query, values)
                connection.commit()
                print("User added successfully.")
            except Error as e:
                print(f"The error '{e}' occurred")
            finally:
                cursor.close()
        else:
            print("Username already exists.")


print("welcome to my library.Whenever you want to exit, enter command 'exit'.")
admin = False
while True:
    first_in = input("If you have already registered, please enter 'l' in the order, otherwise enter 'r' to register.")
    if first_in == 'l':




