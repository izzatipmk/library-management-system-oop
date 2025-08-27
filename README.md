# Library Management System

This is my library management system project that I created for the module 'Principles of Object-Oriented Programming' during my first year of Cyber Security degree. It's a console-based application written in Python that demonstrates the main OOP concepts I learned.


## What the system does

The system has three different types of users:

- Librarians - can add new books, delete books, and check availability of books
- Staff members - can borrow up to 4 books at a time
- Regular members - can borrow up to 2 books at a time

All members can return books and if they return the books late, the system calculates a fine automatically.


## How to run the program

Make sure you install Python, then just run the Python file:
python main.py


## Test login details

I have set up test accounts so you can try different user types features:

- Librarian: username 'admin', password 'admin123'
- Staff: username 'staff1', password 'staff123'
- RegisteredMember: username 'member1', password 'member123'

You can also create a new member account when you run the program.


## The OOP concepts I implemented

This project demonstrated Principles of Object-Oriented Programming:

- Classes and Objects: Book, Member, Staff, Librarian, RegisteredMember, and LibrarySystem.
- Inheritance: Both Staff and RegisteredMember classes inherit from the Member class
- Polymorphism: Both Librarian and Member have different borrowing limits but they use the same methods
- Encapsulation: Each class handles its own data and has specific task roles


## How the fine calculation system works

If you return a book late, the system automatically calculates fines based on duration.

- 31-39 days: £2 fine
- 40-49 days: £4 fine
- 50-59 days: £6 fine
- 60+ days: £10 fine


## Challenges during development

During development, I ran into several issues that I had to debug:

- Data handling: Getting the date calculations working properly for the fine system was tricky for me
- Data management: Applying dictionaries to store all data and ensuring that books moved correctly between available and borrowed books lists
- User authentication: Ensuring that the login system for usernames and passwords match accurately
- Inheritance logic: Making sure that Staff and RegisteredMember classes properly inherited from the Member class while having their dedicated task roles

I documented test case tables in my assignment report where I did 15 different test cases to make sure everything worked.


## What I learned

This project helped me understand how Object-Oriented Programming works like inheritance, encapsulation and polymorphism, and how to structure a larger and complex program using multiple classes to ensure easier way of developing a program. I also learned debugging and testing the code for code errors during the whole process of development. Overall, coding is generally difficult for me since this is my first time learning how to code and implementing OOP principles in my project as I had to do a lot of reading, research, and self practice at home like using ww3schools as guidance to understand how the coding system works which eventually smoothen the process of completing this project.


## Files in this project

- main.py - The complete and main program of the library management system
- README.md - This file


## Academic Use Disclaimer
This project was completed as coursework during my first year of studies. 
It is shared here as part of my learning portfolio. Please do not copy 
this work for your own academic submissions.