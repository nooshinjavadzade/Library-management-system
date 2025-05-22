Library Management System with MySQL and Python

This is a Library Management System built with Python and MySQL. The system allows an admin and regular users to interact with the library database.


Features

Admin Capabilities


The admin can log in using the username admin and the password admin.

Admin functionalities include:

Adding Books: Admin can add new books to the library database.

Deleting Records:

Admin can delete books.

Admin can delete members.

Admin can delete loans.




Viewing Records:

Admin can view the list of books, members, and loans.







Admin access is restricted to the login menu; they cannot register as a regular user.


Regular User Capabilities


Regular users can register through the registration menu.

After registration, users can log in with their username and password.

Regular users can:

Borrow Books: A user can borrow a book only if it is not currently loaned out.

View Available Books: Users can see the list of books in the library.

Only the user can borrow books.




How It Works



Admin Access:


Admin logs in via the login menu.

Once logged in, they gain access to admin-specific features such as adding, deleting, and viewing records.





User Registration:


Regular users register by providing their first name, last name, email, username, and password.

Password must be at least 4 characters long.

Once registered, users can log in with their username and password.





Book Borrowing:


Users can borrow books by entering the book’s ID.

The system checks if the book is currently loaned out:

If the book is available, it is loaned to the user.

If the book is not available, the user is notified that the book is currently loaned out.









System Requirements


Python: Ensure Python is installed on your system.

MySQL Database:

The following tables should exist in your database:

members: Stores user information.

books: Stores book information.

loan: Stores information about borrowed books.




Make sure the database is properly configured with the required tables and columns.




Python Packages:

mysql-connector: For connecting Python to MySQL.

tabulate: For formatting table outputs.

Install it using:        
        bash
        
    
  
      pip install tabulate
    
    
  
  










Setup Instructions



Clone the repository to your local machine:

        
        bash
        
    
  
      git clone https://github.com/yourusername/library-management-system.git
    
    
  
  



Install the required Python packages:

        
        bash
        
    
  
      pip install mysql-connector tabulate
    
    
  
  



Create the necessary tables in your MySQL database:

        
        sql
        
    
  
      CREATE TABLE members (
    memberID INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    email VARCHAR(100),
    join_date DATE
);

CREATE TABLE books (
    bookID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    author VARCHAR(100),
    genre VARCHAR(50)
);

CREATE TABLE loan (
    loanID INT AUTO_INCREMENT PRIMARY KEY,
    book INT NOT NULL,
    user INT NOT NULL,
    land_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book) REFERENCES books(bookID),
    FOREIGN KEY (user) REFERENCES members(memberID)
);
    
    
  
  


    
    
  
  



Run the script:

        
        bash
        
    
  
      python library_system.py
    
    
  
  




Notes


Admin Access: Admin can only log in through the login menu and cannot register as a regular user.

Data Integrity: The system ensures that books cannot be borrowed if they are already loaned out.

Error Handling: Proper error messages are displayed for invalid inputs or database errors.


