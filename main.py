#imports date
from datetime import date


#Book class 
class Book:


    number_of_books = 0


    def __init__(self, book_title, book_author):
        Book.number_of_books +=1
        self.book_id = Book.number_of_books
        self.book_title = book_title
        self.book_author = book_author


    def get_book_id(self):
        return self.book_id


    def get_book_author(self):
        return self.book_author
    

    def addBook():
        book_title = input('Enter book title: ')
        book_author = input('Enter book author: ')
        new_book=({book_title: book_author})
        
        LibrarySystem.available_books.update(new_book)

        print(f'{book_title} has been added to this library.')
        

    def deleteBook():
        book_title = input('Enter title of the book you want to remove: ')
        key = LibrarySystem.available_books.keys()
        value = LibrarySystem.available_books.values()

        if book_title in key:
            book_author = input('Enter book author: ')
            if book_author in value:
                LibrarySystem.available_books.pop(book_title)
                print('This book has been removed from this library.')

        else:
            print('Book not found.')
        


#Librarian class
class Librarian:
                

    #Librarian directed to this menu
    def LibrarianMenu():

        print('LIBRARIAN MENU')
        print("What do you want to do today?")
        print("1. Add a book") #goes to Book.addBook()
        print("2. Check availability of a book") #Displays books available in the system
        print("3. Delete a book") #goes to Book.deleteBook()
        print("4. Quit")

        response = 0
        while response != 8:
            response = int(input("Enter choice: "))

            if response == 1:
                Book.addBook()
                
            elif response ==2:
                print('The available books in this library are: ')
                search = LibrarySystem.available_books.items()
                print(*search, sep='\n')
                
            elif response ==3:
                Book.deleteBook()

            elif response ==4:
                choice = input("Would you like to exit the program Y or N: ")

                if choice == "Y":
                    quit()

                else:
                    Library_menu()
            


#Member class     
class Member():


    number_of_members = 0
   

    def __init__(self, username, password):
        Member.number_of_members += 1
        self.member_id = Member.number_of_members
        self.member_username = username
        self.member_password = password
        

    def get_member_username(self):
        return self.member_username


    def get_member_password(self):
        return self.member_password


    #Function that stores books borrowed to the system
    def get_borrowBook(username, password, borrow_bookTitle, borrow_bookAuthor):

        LibrarySystem.borrowed_books.update({borrow_bookTitle: borrow_bookAuthor})
        LibrarySystem.available_books.pop(borrow_bookTitle, borrow_bookAuthor)

        book_count = LibrarySystem.borrowed_books.items()
        member_borrowed_amount = len(book_count)
        LibrarySystem.member_books.update({username: member_borrowed_amount})

        print(f'{borrow_bookTitle} has been issued to {username}. Please return within 30 days. Thank you')

        if username in LibrarySystem.staff_members.keys():
            if password in LibrarySystem.staff_members.values():
                Staff.check_out_book(username, password, member_borrowed_amount)

        elif username in LibrarySystem.members.keys():
            if password in LibrarySystem.members.values():
                RegisteredMember.check_out_book(username, password, member_borrowed_amount)


    #Function determines if members are fined
    def get_returnBook(username, return_bookTitle, return_bookAuthor):

        print('Enter the date when you borrowed this book:')
                            
        Day = int(input('Day: '))
        Month = int(input('Month: '))
        Year = int(input('Year: '))
        date_Borrowed = date(Year, Month, Day)

        print('Enter the date you return this book:')
        day = int(input('Day: '))
        month = int(input('Month: '))
        year = int(input('Year: '))
        date_Returned = date(year, month, day)

        LibrarySystem.borrowed_books.pop(return_bookTitle, return_bookAuthor)
        LibrarySystem.available_books.update({return_bookTitle: return_bookAuthor})
                            
        days_borrowed = date_Returned - date_Borrowed
                            
        days = days_borrowed.days

        Member.get_totalDaysBorrowed(username, days)


    #Get duration of borrowing books which determines if members are fined
    def get_totalDaysBorrowed(username, days):

        if days > 30:
            Member.give_fine(username, days)
                                
        else:
            print('Thank you for returning this book.')



    #Members issued fine when returning books late
    def give_fine(username, days):

        fine = 0

        print(f'{username} has borrowed this book for: {days} days')
        print('You need to pay fine for returning this book late.')
        
        if 30 < days <= 39:
            amount_of_fine = fine + 2
            print(f'The amount of fine you need to pay is £{amount_of_fine}')

        elif 40 <= days <= 49:
            amount_of_fine = fine + 4
            print(f'The amount of fine you need to pay is £{amount_of_fine}')

        elif 50 <= days <= 59:
            amount_of_fine = fine + 6
            print(f'The amount of fine you need to pay is £{amount_of_fine}')

        elif days > 59:
            amount_of_fine = fine + 10
            print(f'The amount of fine you need to pay is £{amount_of_fine}')



#Staff class which inherits the constructor from the Member class
class Staff(Member):


    def __init__(self, username, password, dep):
        super().__init__(username, password)
        self.department = dep


    #Staff can only check out up to 4 books
    def check_out_book(username, password, member_borrowed_amount):
        print(f'CURRENT BOOK BORROWED COUNT: {member_borrowed_amount}')

        if member_borrowed_amount > 3:
            print('You have reached your maximum number of books limit. ')
            print('You are not allowed to borrow another book')

        else:
            LibrarySystem.MemberMenu(username, password)



#RegisteredMember class which inherits the constructor from Member class
class RegisteredMember(Member):


    def __init__(self, username, password):
        super().__init__(username, password)


    #RegisteredMember can only check out up 2 books
    def check_out_book(username, password, member_borrowed_amount):
        print(f'CURRENT BOOK BORROWED COUNT: {member_borrowed_amount}')

        if member_borrowed_amount > 1:
            print('You have reached the maximum book limit.')
            print('You are not allowed to borrow another book')

        else:
            LibrarySystem.MemberMenu(username, password)



#LibrarySystem class which stores all data
class LibrarySystem:


    date_borrowed_books=[] #List of dates when borrowing books
    date_returned_books=[] #List of dates when returning books

    staff_members={'staff1': 'staff123'} #Stores staff username and password
    members={'member1':'member123'} #Stores registered member username and password
    librarian = {'admin':'admin123'} #Stores librarian username and password
    available_books={'Python Programming':'John K', 'Cyber Security':'Alex R'} #Stores books including title and author
    borrowed_books={} #Stores borrowed books
    member_books={} #Stores borrowed books to a specific member


    #Search if login details entered by registered members matches with the system
    def find_users():
        username = input('Username: ')
        keys = LibrarySystem.members.keys()
        values = LibrarySystem.members.values()

        if username in keys:
            password = input('Please enter your password: ')

            if password in values:
                print(f'Welcome back {username}')
                confirm=input('Do you want to continue? Y or N: ')

                if confirm == 'Y':
                    Member(username, password)
                    LibrarySystem.MemberMenu(username, password)

                else:
                    LibrarySystem.logout()

            else:
                print('INVALID PASSWORD. Please create a new account.')
                LibrarySystem.register()

        else:
            print('INVALID. Please create a new account.')
            LibrarySystem.register()


    #Search if login details entered by staff matches with the system
    def find_staff():
        username = input('Username: ')
        keys = LibrarySystem.staff_members.keys()
        values = LibrarySystem.staff_members.values()

        if username in keys:
            password = input('Please enter your password: ')

            if password in values:
                dep = input('What department are you in?: ')
                print(f'Welcome back {username}')
                confirm = input('Do you want to continue? Y or N: ')

                if confirm == 'Y':
                    Staff(username, password, dep)
                    Staff.number_of_members +=1 
                    LibrarySystem.MemberMenu(username, password)

                else:
                    LibrarySystem.logout()

            else:
                print('INVALID PASSWORD')
        
        else:
            print('INVALID')


    #Search if login details entered by librarian matches with the system
    def find_librarian():
        librarian_username = input('Please enter your username: ')
        key = LibrarySystem.librarian.keys()
        value = LibrarySystem.librarian.values()

        if librarian_username in key:
            librarian_password = input('Enter password: ')

            if librarian_password in value:
                print(f'Welcome back {librarian_username}')
                choice = input('Do you wish to continue? Y or N: ')

                if choice == 'Y':
                    Librarian.LibrarianMenu()

                else:
                    LibrarySystem.logout()

            else:
                print('Incorrect password')

        else:
            print('INVALID')
            Library_menu()


    #Create account for new users
    def register():

        print("Welcome to the Library System. Please sign in")
        username_input = input("Username: ")
        password_input = input("Password: ")
        LibrarySystem.members.update({username_input:password_input})

        print("You have successfully become a member.")
        LibrarySystem.login()


    #General login for members
    def login():
        print('Choose from the option below:')
        print('1. Staff')
        print('2. Registered Member')

        choice = int(input('Enter option 1 or 2: '))

        if choice == 1:
            LibrarySystem.find_staff()

        else:
            print("Please enter existing account")
            LibrarySystem.find_users()
        

    #Logout for all users 
    def logout():
        Library_menu()


    #Login for Librarian only
    def librarian_login():
        print('LIBRARIAN LOGIN')
        LibrarySystem.find_librarian()
         
    
    #MemberMenu accessed when staff or registered member login
    def MemberMenu(username, password): 

        print('MEMBER MENU')
        print(f"What do you want to do today {username}")
        print("1. Borrow a book") #Members can borrow books
        print("2. Return a book") #Members can return books
        print("3. Quit")

        response= 0

        while response != 3:

            response = int(input("Enter choice: "))

            if response ==1:

                print('The available books in this library are: ')
                booksList=LibrarySystem.available_books.items()
                print(*booksList, sep='\n')

                keys = LibrarySystem.available_books.keys()
                values = LibrarySystem.available_books.values()
                borrow_bookTitle=input('Please enter the title of the book you would like to borrow: ')

                if borrow_bookTitle in keys:
                    borrow_bookAuthor = input('Enter the author of the book: ')

                    if borrow_bookAuthor in values:
                        confirm = input('Please confirm if you would like to borrow this book Y or N: ')

                        if confirm == 'Y':
                            Member.get_borrowBook(username, password, borrow_bookTitle, borrow_bookAuthor)

                        else: 
                            LibrarySystem.MemberMenu()

                    else:
                        print('Book not found')
                          
                else:
                    print('Book not found')
                        
               
            elif response == 2:

                keys = LibrarySystem.borrowed_books.keys()
                values = LibrarySystem.borrowed_books.values()
                return_bookTitle = input('Please enter the title of the book you would like to return: ')

                if return_bookTitle in keys:
                    return_bookAuthor = input('Enter the author of the book: ')

                    if return_bookAuthor in values:
                        confirm = input('Please confirm if you would like to return this book Y or N: ')

                        if confirm == 'Y':
                            Member.get_returnBook(username, return_bookTitle, return_bookAuthor)

                        else:
                            LibrarySystem.MemberMenu()
                                        
                else:
                    print('Book does not exist')


            elif response == 3:
                choice = input("Would you ike to exit the program Y or N: ")
                if choice == "Y":
                    quit()
                else:
                    Library_menu()


#Library_menu where users will be first taken to
def Library_menu():

    print("Welcome to the Library System")
    print("Please select from the following options:")
    print("1. Librarian")
    print("2. Member")

    user_option = int(input("Please enter the option: 1 or 2: "))

    if user_option==1:
        LibrarySystem.librarian_login()

    else:
        LibrarySystem.login()
       
           
            
#This runs the program
if __name__=='__main__':

    Library_menu()

    