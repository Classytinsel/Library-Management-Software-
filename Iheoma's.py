#class to represent a book
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False

#class to represent the library
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book removed successfully.")
        else:
            print("Book not found in the library.")

    def borrow_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.is_available:
                book.is_available = False
                print(f"You have borrowed '{book.title}'.")
            else:
                print("The book is already borrowed.")
        else:
            print("Book not found in the library.")

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if not book.is_available:
                book.is_available = True
                print(f"You have returned '{book.title}'.")
            else:
                print("The book is already in the library.")
        else:
            print("Book not found in the library.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book_id, book in self.books.items():
                print(book)

#Sample usage
if __name__ == "__main__":
    library = Library()

    book1 = Book("Python Crash Course", "Eric Matthes", "978-1593276034")
    book2 = Book("Clean Code", "Robert C. Martin", "978-0132350884")

    library.add_book(book1)
    library.add_book(book2)

    while True:
        print("\nWelcome to Iheoma's Library Management System")
        print("1. Search Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Remove Book")
        print("5. Display all Books")
        print("6. Add Book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            book_id = input("Enter the book ID: ")
            book = Book(title, author, book_id)
            library.search_book(book)

        elif choice == "2":
            book_id = input("Enter the book title you want to borrow: ")
            library.borrow_book(book_title)

        elif choice == "3":
            book_id = input("Enter the book title you want to return: ")
            library.return_book(book_title)

        elif choice == "4":
            book_id = input("Enter the book title you want to remove: ")
            library.remove_book(book_title)

        elif choice == "5":
            library.display_all_books()
            
        elif choice == "6":
            book_id = input("Enter the book title you want to add: ")

        elif choice == "0":
            print("Thank you for using the Iheoma's Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()