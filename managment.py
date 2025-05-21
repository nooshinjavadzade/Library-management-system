import mysql.connector
from mysql.connector import Error
from datetime import datetime
import sys
import hashlib

def connection(host_name, user_name, user_password, db_name):
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

connectionn = connection("localhost", "root", "nooshin1385", "library")
if connectionn is None:
    print("Failed to connect to the database.")
    sys.exit(1)

cursor = connectionn.cursor()

def closing():
    if connectionn:
        connectionn.close()
        print("Connection closed.")

class member:
    def __init__(self, firstname, lastname, username, password, email):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.email = email
        self.join_date = datetime.now().strftime('%Y-%m-%d')

    def if_join(self, username):
        query = "SELECT COUNT(*) FROM members WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result[0] > 0:
            return True
        else:
            return False

    def add_user(self):
        if not self.if_join(self.username):
            query = "INSERT INTO members (firstname, lastname, username, password, join_date, email) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (self.firstname, self.lastname, self.username, self.password, self.join_date, self.email)
            try:
                cursor.execute(query, values)
                connectionn.commit()
                print("User added successfully.")
            except Error as e:
                print(f"The error '{e}' occurred")
        else:
            print("Username already exists.")

def check_user_password(username, password):
    query = "SELECT password FROM members WHERE username = %s"
    try:
        cursor.execute(query, (username,))
        result = cursor.fetchone()
    except Error as e:
        print(f"Database error: {e}")
        return False

    if result is not None:
        stored_password = result[0]
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return stored_password == hashed_password
    else:
        return False

print("Welcome to my library. Whenever you want to exit, enter command 'exit'.")
admin = False
while True:
    first_in = input("If you have already registered, please enter 'l', otherwise enter 'r' to register: ")
    if first_in == 'l':
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if username == 'admin' and password == 'admin':
            admin = True
            break
        else:
            if check_user_password(username, password):
                print("You have successfully logged in.")
                break
            else:
                print("Invalid username or password.")
    elif first_in == 'r':
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        email = input("Please enter your email: ")
        username = input("Please enter your username: ")
        password = input("Please enter your password (must have at least 4 characters): ")
        if len(password) < 4:
            print("Password must have at least 4 characters.")
            continue
        new_user = member(first_name, last_name, username, password, email)
        new_user.add_user()
        break
    elif first_in == 'exit':
        closing()
        sys.exit(0)
    else:
        print("Invalid input.")