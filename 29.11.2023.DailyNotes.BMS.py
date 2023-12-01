#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Banking Management System

#Sample1

class BankAccount:
    def __init__(self, account_number, holder_name, phone_number, password, bin_number, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.phone_number = phone_number
        self.password = password
        self.bin_number = bin_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def transfer(self, recipient, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            print(f"Transferred ${amount} to {recipient.holder_name}. New balance: ${self.balance}")
        else:
            print("Invalid transfer amount or insufficient funds.")

    def check_balance(self):
        print(f"Account Balance for {self.holder_name}: ${self.balance}")

    def change_password(self, new_password):
        self.password = new_password
        print("Password changed successfully.")

    def change_bin_number(self, new_bin_number):
        self.bin_number = new_bin_number
        print("BIN number changed successfully.")


# Example usage:
if __name__ == "__main__":
    # Creating accounts
    account1 = BankAccount(1001, "Vijay", "1234567890", "pass123", "1234")
    account2 = BankAccount(1002, "Kate", "9876543210", "pass456", "5678", 500)

    # Performing transactions
    account1.deposit(100)
    account2.transfer(account1, 50)
    account1.check_balance()
    account2.check_balance()

    # Changing password and BIN
    account1.change_password("newpass")
    account1.change_bin_number("4321")
    


# In[1]:


# Banking Management System Sample 1

class BankManagement:
    def __init__(self):
        self.client_details = []
        self.cash = 100
        self.loggedin = False

    def register(self, name, phone_number, password):
        condition = True
        if len(str(phone_number)) != 10:
            print('Invalid phone number')
            condition = False
        if not (5 <= len(str(password)) <= 18):
            print('Invalid password')
            condition = False
        if condition:
            self.client_details = [name, phone_number, password, self.cash]
            with open(f'{name}.txt', 'w') as f:
                for details in self.client_details:
                    f.write(str(details) + '\n')

    def login(self, name, phone_number, password):
        self.loggedin = True
        with open(f'{name}.txt', 'r') as f:
            details = f.read()
            self.client_details = str(details).split('\n')
            if str(phone_number) in str(self.client_details) and str(password) in str(self.client_details):
                print(f'{name} has logged in successfully')

    def add_cash(self, name, amount):
        if amount > 0:
            self.cash += amount
            with open(f'{name}.txt', 'r+') as f:
                f.seek(0)
                x = f.read()
                z = x.rfind('\n', 0, -1)
                f.seek(z)
                f.write('\n' + str(self.cash))
                f.seek(0)
                zz = f.read()
                print(zz)
            print('Amount has been added')
        else:
            print('Please enter a valid amount')

    def update_phone_number(self, new_phone_number, name):
        if len(str(new_phone_number)) == 10:
            print('Phone number updated')
            with open(f'{name}.txt', 'r+') as f:
                f.seek(0)
                x = f.read()
                z = x.find('\n', x.find('\n') + 1)
                f.seek(z)
                f.write('\n' + str(new_phone_number))
                f.seek(0)
                zz = f.read()
                # print(zz)


# Example usage:
if __name__ == "__main__":
    bank = BankManagement()

    # Register a new user
    bank.register("Vijay", "1234567890", "password123")

    # Login
    bank.login("Vijay", "1234567890", "password123")

    # Add cash
    bank.add_cash("Vijay", 50)

    # Update phone number
    bank.update_phone_number("9876543210", "Vijay")



# In[3]:


#task1 BMS

class BankManagement:
    def __init__(self):
        self.client_details = []
        self.cash = 100
        self.loggedin = False

    def register(self, name, phone_number, password):
        condition = True
        if len(str(phone_number)) != 10:
            print('Invalid phone number')
            condition = False
        if not (5 <= len(str(password)) <= 18):
            print('Invalid password')
            condition = False
        if condition:
            self.client_details = [name, phone_number, password, self.cash]
            with open(f'{name}.txt', 'w') as f:
                for details in self.client_details:
                    f.write(str(details) + '\n')

    def login(self, name, phone_number, password):
        self.loggedin = True
        with open(f'{name}.txt', 'r') as f:
            details = f.read()
            self.client_details = str(details).split('\n')
            if str(phone_number) in str(self.client_details) and str(password) in str(self.client_details):
                print(f'{name} has logged in successfully')

    def add_cash(self, name, amount):
        if amount > 0:
            self.cash += amount
            with open(f'{name}.txt', 'r+') as f:
                f.seek(0)
                x = f.read()
                z = x.rfind('\n', 0, -1)
                f.seek(z)
                f.write('\n' + str(self.cash))
                f.seek(0)
                zz = f.read()
                print(zz)
            print('Amount has been added')
        else:
            print('Please enter a valid amount')

    def update_phone_number(self, new_phone_number, name):
        if len(str(new_phone_number)) == 10:
            print('Phone number updated')
            with open(f'{name}.txt', 'r+') as f:
                f.seek(0)
                x = f.read()
                z = x.find('\n', x.find('\n') + 1)
                f.seek(z)
                f.write('\n' + str(new_phone_number))
                f.seek(0)
                zz = f.read()
                # print(zz)


# Example usage:
if __name__ == "__main__":
    bank = BankManagement()

    # Register a new user
    bank.register("Vijay", "1234567890", "password123")

    # Login
    bank.login("Vijay", "1234567890", "password123")

    # Add cash
    bank.add_cash("Vijay", 50)

    # Update phone number
    bank.update_phone_number("9876543210", "Vijay")


# In[4]:


#Task 3 LMS

class LibraryManagement:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}
        self.loggedin = False

    def add_book(self, book_title, quantity):
        if book_title not in self.books:
            self.books[book_title] = quantity
            print(f"Added {quantity} copies of '{book_title}' to the library.")
        else:
            self.books[book_title] += quantity
            print(f"Added {quantity} copies to the existing stock of '{book_title}'.")

    def borrow_book(self, book_title, quantity):
        if self.loggedin:
            if book_title in self.books and self.books[book_title] >= quantity:
                if book_title not in self.borrowed_books:
                    self.borrowed_books[book_title] = quantity
                else:
                    self.borrowed_books[book_title] += quantity

                self.books[book_title] -= quantity
                print(f"Borrowed {quantity} copies of '{book_title}'.")
            else:
                print(f"Sorry, '{book_title}' is not available or insufficient stock.")
        else:
            print("Please log in first.")

    def return_book(self, book_title, quantity):
        if self.loggedin:
            if book_title in self.borrowed_books and self.borrowed_books[book_title] >= quantity:
                self.borrowed_books[book_title] -= quantity
                self.books[book_title] += quantity
                print(f"Returned {quantity} copies of '{book_title}'.")
            else:
                print(f"You have not borrowed {quantity} copies of '{book_title}'.")
        else:
            print("Please log in first.")

    def view_available_books(self):
        print("Available Books:")
        for book_title, quantity in self.books.items():
            print(f"{book_title}: {quantity} copies")

    def login(self):
        self.loggedin = True
        print("Logged in successfully.")


# Example usage:
if __name__ == "__main__":
    library = LibraryManagement()

    # Add books to the library
    library.add_book("Python Programming", 5)
    library.add_book("Data Science with Python", 3)

    # Log in
    library.login()

    # Borrow books
    library.borrow_book("Python Programming", 2)
    library.borrow_book("Data Science with Python", 1)

    # View available books
    library.view_available_books()

    # Return books
    library.return_book("Python Programming", 1)

    # View available books after returning
    library.view_available_books()


# In[8]:


#LMS 4

class LibraryManagement:
    def __init__(self):
        self.books = {}

    def add_book(self, title, quantity):
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity

    def view_available_books(self):
        print("Available Books:")
        for title, quantity in self.books.items():
            print(f"{title}: {quantity} available")

class LibraryUser:
    def __init__(self, username):
        self.username = username
        self.borrowed_books = {}

    def login(self):
        # Placeholder for login functionality
        print(f"{self.username} logged in.")

    def borrow_book(self, library, title, quantity):
        if title in library.books and library.books[title] >= quantity:
            if title in self.borrowed_books:
                self.borrowed_books[title] += quantity
            else:
                self.borrowed_books[title] = quantity
            library.books[title] -= quantity
            print(f"{self.username} borrowed {quantity} copies of '{title}'")
        else:
            print(f"Sorry, '{title}' is not available in sufficient quantity.")

    def return_book(self, library, title, quantity):
        if title in self.borrowed_books and self.borrowed_books[title] >= quantity:
            self.borrowed_books[title] -= quantity
            library.books[title] += quantity
            print(f"{self.username} returned {quantity} copies of '{title}'")
        else:
            print(f"You can't return {quantity} copies of '{title}'. Check your borrowed books.")

    def view_borrowed_books(self, library):
        print(f"{self.username}'s Borrowed Books:")
        for title, quantity in self.borrowed_books.items():
            print(f"{title}: {quantity} copies")

if __name__ == "__main__":
    library = LibraryManagement()

    # Add books to the library
    library.add_book("Python Programming", 5)
    library.add_book("Data Science with Python", 3)

    # User login
    vijay = LibraryUser("Vijay")
    vijay.login()

    # User borrows books
    vijay.borrow_book(library, "Python Programming", 2)
    vijay.borrow_book(library, "Data Science with Python", 1)

    # View available books
    library.view_available_books()

    # User returns books
    vijay.return_book(library, "Python Programming", 1)

    # View borrowed books after returning
    vijay.view_borrowed_books(library)

