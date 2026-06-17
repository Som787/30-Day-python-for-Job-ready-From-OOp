 #**Library Management System**: Model Books, Members, and Loans. Handle checking in/out books.
class Book:
  def __init__(self,book_id,title,author):
    self.book_id=book_id
    self.author=author
    self.title=title
    self.is_available=True
  def __str__(self):
    return f"{self.title} by {self.author} {self.book_id}"
class Member:
  def __init__(self,member_id,name):
    self.member_id=member_id
    self.name=name
  def __str__(self):
    return f"{self.name} (Member Id: {self.member_id})"
class Loan:
  def __init__(self,book,member):
    self.book=book
    self.member=member

class Library:
  def __init__(self):
    self.books={}
    self.members={}
    self.loans=[]
  def add_book(self,book):
    self.books[book.book_id]=book
  def add_member(self,member):
    self.members[member.member_id]=member
  def checkout_book(self,book_id,member_id):
    if book_id not in self.books:
      return "Books Not Found"
    if member_id not in  self.members:
      return "Members not Found"
    book=self.books[book_id]
    member=self.members[member_id]
    if not book.is_available:
      return "Book is already Loaned"
    book.is_available=False
    loan=Loan(book,member)
    self.loans.append(loan)
    return f"{book.title} checked out to {member.name}"
  def checkin_book(self,book_id):
    if book_id not in self.books:
      return "book is not in library"
    book=self.books[book_id]
    if book.is_available:
      return "Book is already in Library"
    book.is_available=True
    # Remove loan record
    self.loans = [loan for loan in self.loans if loan.book.book_id != book_id]
    return f"{book.title} has been checked in."
  def list_books(self):
    return [str(book) + (" — Available" if book.is_available else " — Loaned Out") for book in self.books.values()]
  
library = Library()

# Add books
library.add_book(Book(1, "1984", "George Orwell"))
library.add_book(Book(2, "The Hobbit", "J.R.R. Tolkien"))

# Add members
library.add_member(Member(101, "Somraj"))
library.add_member(Member(102, "Aarav"))

# Checkout
print(library.checkout_book(1, 101))

# List books
for b in library.list_books():
    print(b)

# Checkin
print(library.checkin_book(1))

