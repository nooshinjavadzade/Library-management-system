import mysql.connector
from mysql.connector import Error
from datetime import datetime
import sys
from tabulate import tabulate

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
        self.password = password
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

class book:
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre

    def add_book(self):
        query = "INSERT INTO books (book_name, author, gener) VALUES (%s, %s, %s)"
        values = (self.name, self.author, self.genre)
        try:
            cursor = connectionn.cursor()
            cursor.execute(query, values)
            connectionn.commit()
            print("Book added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

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
        return stored_password == password
    else:
        return False

def show_books():
    query = "SELECT * FROM books"
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            print(tabulate(result, headers=["ID", "Name", "Author", "Genre"], tablefmt="fancy_grid"))
        else:
            print("No books found.")
    except Error as e:
        print(f"Database error: {e}")
        return False

def show_members():
    query = "SELECT * FROM members"
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            print(tabulate(result, headers=["ID" , "first name" , "last name" , "email" ,"username" , "password", "join date"], tablefmt="fancy_grid"))
        else:
            print("No members found.")
    except Error as e:
        print(f"Database error: {e}")
        return False

def show_loans():
    query = "SELECT * FROM loan"
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            print(tabulate(result, headers=["loan ID" , "book ID" , "memberID" , "date borrowed" , "date return"] , tablefmt="fancy_grid"))
        else:
            print("No loans found.")
    except Error as e:
        print(f"Database error: {e}")
        return False

def delete_book(ID):
    query = "DELETE FROM books WHERE bookID = %s"
    try:
        cursor.execute(query, (ID,))
        if cursor.rowcount == 0:
            print("No book found with the given ID.")
        else:
            connectionn.commit()
            print("Book deleted successfully.")
    except Error as e:
        print(f"The error '{e}' occurred")

def delete_member(ID):
    query = "DELETE FROM members WHERE memberID = %s"
    try:
        cursor.execute(query, (ID,))
        if cursor.rowcount == 0:
            print("No member found with the given ID.")
        else:
            connectionn.commit()
            print("Member deleted successfully.")
    except Error as e:
        print(f"The error '{e}' occurred")

def delete_loan(ID):
    query = "DELETE FROM loan WHERE loanID = %s"
    try:
        cursor.execute(query, (ID,))
        if cursor.rowcount == 0:
            print("No loan found with the given ID.")
        else:
            connectionn.commit()
            print("Loan deleted successfully.")
    except Error as e:
        print(f"The error '{e}' occurred")

def get_member_id( username):
    cursor = connectionn.cursor()
    query = "SELECT memberID FROM members WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        print("User not found.")
        return None


def land_book(bookID, userID):
    cursor = connectionn.cursor()
    query = "SELECT return_date FROM loan WHERE book = %s ORDER BY land_date DESC LIMIT 1"
    cursor.execute(query, (bookID,))
    result = cursor.fetchone()
    if result is None or result[0] is not None:
        try:
            land_date = datetime.now().strftime('%Y-%m-%d')
            query = "INSERT INTO loan (book, user, land_date) VALUES (%s, %s, %s)"
            cursor.execute(query, (bookID, userID, land_date))
            connectionn.commit()
            print("Book borrowed successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("The book is currently not available for borrowing.")


def return_book(loanID):
    try:
        return_date = datetime.now().strftime('%Y-%m-%d')
        query = "UPDATE loan SET return_date = %s WHERE loanID = %s"
        cursor.execute(query, (return_date, loanID))
        if cursor.rowcount == 0:
            print("No loan found with the given ID.")
        else:
            connectionn.commit()
            print(f"Book with loan ID {loanID} has been successfully returned.")
    except Error as e:
        print(f"An error occurred: {e}")


def show_user_loans(userID):
    try:
        query = """
            SELECT loan.loanID, books.bookID, books.book_name, books.author 
            FROM loan 
            INNER JOIN books ON loan.book = books.bookID
            WHERE loan.user = %s AND loan.return_date IS NULL
        """
        cursor.execute(query, (userID,))
        results = cursor.fetchall()
        if not results:
            print("You have no pending loans.")
            return
        headers = ["Loan ID", "Book ID", "Book Name", "Author"]
        print("Your current borrowed books are:")
        print(tabulate(results, headers=headers, tablefmt="grid"))
        print("To return a book, use the corresponding Loan ID.")
    except Error as e:
        print(f"An error occurred: {e}")


def check_username(username):
        query = "SELECT COUNT(*) FROM members WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result[0] > 0:
            return True
        else:
            return False


#start from here
print("Welcome to my library. Whenever you want to exit, enter command 'exit'.")
admin = False
user_name = " "
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
                user_name = username
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
        if check_username (username):
            print("Your username has been registered.")
            continue
        if len(password) < 4:
            print("Password must have at least 4 characters.")
            continue
        new_user = member(first_name, last_name, username, password, email)

        user_name = username
        new_user.add_user()
        break
    elif first_in == 'exit':
        closing()
        sys.exit(0)
    else:
        print("Invalid input.")


while admin:
    print("Dear admin, welcome!")
    ad_in = input("Enter command 'b' to go to the list of books.\n "
                  "Enter command 'm' to go to the list of library members.\n"
                  " Enter command 'l' to see the list of loans:")
    if ad_in == "exit":
        closing()
        sys.exit(0)

    if ad_in == 'b':
        print("List of books:")
        show_books()
        print("To delete a book, enter the command -d <book id> .\n"
              "To add a book, enter the command -add."
              "\n Enter command 'back' to return to the admin menu:")
        ad_in2 = input("Enter your choice: ")
        if ad_in2 == "back":
            continue
        elif ad_in2 == '-add':
            name = input("Enter your book name: ")
            author = input("Enter your book author: ")
            genre = input("Enter your book genre: ")
            new_book = book(name, author, genre)
            new_book.add_book()
            continue
        elif ad_in2.startswith("-d"):
            book_id = ad_in2.split("-d")[1].strip()
            book_id = int(book_id)
            delete_book(book_id)
            continue
        else:
            print("Invalid input.")

    if ad_in == 'm':
        show_members()
        ad_in3 = input("To delete a member, enter the command -d <member id> .\n"
              " Enter command 'back' to return to the admin menu: ")
        if ad_in3 == "back":
            continue
        elif ad_in3.startswith("-d"):
            member_id = ad_in3.split("-d")[1].strip()
            member_id = int(member_id)
            delete_member(member_id)
            continue
        else:
            print("Invalid input.")

    if ad_in == 'l':
        show_loans()
        in_4 = input("To delete a loan, enter the command -d <loan id> .\n"
                     "Enter command 'back' to return to the admin menu: ")
        if in_4 == "back":
            continue
        elif in_4.startswith("-d"):
            loan_id = in_4.split("-d")[1].strip()
            loan_id = int(loan_id)
            delete_loan(loan_id)
            continue
        else:
            print("Invalid input.")


while not admin:
    print("Welcom to my library.")
    show_books()
    user_in = input("To exit, enter the command 'exit'.\n "
                    "To return a book, enter the command 'return'.\n "
                    " To borrow a book, enter the command 'borrow': ")
    if user_in.lower() == "exit":
        closing()
        sys.exit(0)
    elif user_in.lower() == "borrow":
        x = input("Enter your book id: ")
        land_book(x,get_member_id(user_name))
    elif user_in.lower() == "return":
        show_user_loans(get_member_id(user_name))
        y = input("Enter your loan id: ")
        return_book(y)




closing()








