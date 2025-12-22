# Create a class named Library
class Library:

    # Constructor to initialize book details
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author

    # Method 1: Display book information
    def show_details(self):
        print("Book Name:", self.book_name)
        print("Author:", self.author)

    # Method 2: Check availability
    def availability(self):
        print("The book is available in the library.")


# Creating objects of Library class
book1 = Library("Python Basics", "Guido van Rossum")
book2 = Library("Java", "James Gosling")

# Calling methods
book1.show_details()
book1.availability()

book2.show_details()
book2.availability()
  