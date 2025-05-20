show databases ;
use library;
show tables ;
create table members(
    memberID int primary key auto_increment,
    firstname varchar(30) not null ,
    lastname varchar(30) not null ,
    email varchar(50),
    username varchar(50) not null ,
    password varchar(5) not null ,
    join_date date not null ,
    check (CHAR_LENGTH(password) = 4 )
);
create table books(
    bookID int primary key auto_increment,
    book_name varchar(50) not null ,
    author varchar(50),
    gener varchar(30)
);
create table loan(
    loanID int primary key auto_increment,
    book int,
    user int,
    foreign key (user) references members(memberID),
    foreign key (book) references books(bookID),
    land_date date not null ,
    return_date date not null
);


