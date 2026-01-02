# Create a class named Book
class Book:

    # Constructor to initialize book details
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True   # Boolean to track availability

    # Method to issue the book
    def issue_book(self):
        if self.is_available:
            self.is_available = False
            print("Book issued successfully.")
            return True
        else:
            print("Book is already issued. Cannot issue again.")
            return False

    # Method to return the book
    def return_book(self):
        self.is_available = True
        print("Book returned successfully.")

    # Method to display book status
    def display_status(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available:", self.is_available)


# Creating book objects
book1 = Book(101, "Python Basics", "Guido van Rossum")

# Display status
book1.display_status()

# Issue the book
book1.issue_book()

# Try issuing again
book1.issue_book()

# Return the book
book1.return_book()

# Display status again
book1.display_status()
