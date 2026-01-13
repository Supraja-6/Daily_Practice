""" Set 4 (Library Management System)
A library handles book borrowing and returning.
Scenario:
Class Book with attributes title, author, is_available


Class Member with borrow and return methods


Requirements:
Prevent borrowing if book is unavailable


Track number of borrowed books per member

Apply fine logic using encapsulation
"""
from abc import ABC, abstractmethod 
class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    @abstractmethod
    def get_book_details(self):
        pass

class LibraryBook(Book):
    def get_book_details(self):
        return f"{self.title} by {self.author}"
    
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_count = 0
        self.__fine = 0 

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_count += 1
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available")

    def return_book(self, book, late_days):
        book.is_available = True
        self.borrowed_count -= 1

        if late_days > 0:
            fine_amount = late_days * 5   # I have added fine per day as 5
            self.__fine += fine_amount
            print(f"Because of Late Return, Fine is added: ₹{late_days * 5}")

        print(f"{self.name} returned '{book.title}'")
    
    def get_fine(self):
        return self.__fine

book1 = LibraryBook("Basics of Python", "Guido Van")
member1 = Member("Supraja")
book2 = LibraryBook("Python From Basics to Advance", "Guido")
member2 = Member("Kotturu")

member1.borrow_book(book1)
member2.borrow_book(book2)
member1.borrow_book(book1)   # not allowed
member2.borrow_book(book2)
member1.return_book(book1, late_days=3)
member2.return_book(book2, late_days=2)

print("Books borrowed:", member1.borrowed_count)
print("Total fine:", member1.get_fine())
print("Books borrowed:", member2.borrowed_count)
print("Total fine:", member2.get_fine())