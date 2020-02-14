class Book:
    numberOfBooks = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.numberOfBooks += 1

    def bookInfo(self):
        print("Book title:", self.title)
        print("Book author:", self.author, "\n")

# Create a virtual book store
b1 = Book("Great Expectations", "Charles Dickens")
b2 = Book("War and Peace", "Leo Tolstoy")
b3 = Book("Middlemarch", "George Eliot")

# call member functions for each object
b1.bookInfo()
b2.bookInfo()
b3.bookInfo()

print("BookStore.noOfBooks:", Book.numberOfBooks)
