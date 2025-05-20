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
    def __init__(self, firstname,lastname, age , username , password , join_date):
        self.firstname = firstname
        self.age = age
        self.username = username
        self.password = password
        self.join_date = datetime.now().strftime('%Y-%m-%d')

    def add_user(self):
        if not self.if_join():
            cursor = connection.cursor()
            query = "INSERT INTO members (firstname, lastname, age, username, password, join_date) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (self.firstname, self.lastname, self.age, self.username, self.password, self.join_date)
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

    def check_password(self, username, password):
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM members WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        cursor.close()

        if result[0] > 0:
            return True
        else:
            return False



class admin:
    def __init__(self, firstname, lastname,username , password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    def if_join(self, username):
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM admins WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        cursor.close()

        if result[0] > 0:
            return True
        else:
            return False

    def check_password(self, username, password):
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM admins WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        cursor.close()

        if result[0] > 0:
            return True
        else:
            return False

    def add_admin(self):
        if not self.if_join():
            cursor = connection.cursor()
            query = "INSERT INTO admins (firstname, lastname , username, password) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (self.firstname, self.lastname, self.username, self.password)
            try:
                cursor.execute(query, values)
                connection.commit()
                print("Admin added successfully.")
            except Error as e:
                print(f"The error '{e}' occurred")
            finally:
                cursor.close()
        else:
            print("Username already exists.")




print("welcome to my library.Whenever you want to exit, enter command 'exit'.")
admin = False
while True:
    first_in = input("If you are a member input 'm' and if you are a admin input 'a':")
    if first_in == "m":
        sec_in = input("If you have already registered, please enter l in the order, otherwise enter r to register.")
        if sec_in == "r":
            fname = input("Please enter first name: ")
            lname = input("Please enter last name: ")
            age = input("Please enter age: ")
            username = input("Please enter username: ")
            password = input("Please enter password: ")
            new_user = user(fname, lname, age, username, password)
            break
        if sec_in == "l":
            username = input("Please enter username: ")
            password = input("Please enter password: ")
            



    elif first_in == "a":


    elif first_in == "exit":
        sys.exit(0);

    else:
        print("Invalid input.")
