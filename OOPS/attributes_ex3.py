# Create a Library class with book name and number of copies.
# Create methods to issue, return and print available copies.

class Library:
    def __init__(self, book, copies):
        self.book = book
        self.copies = copies

    def issue(self, count):
        self.copies -= count
        print(count, "book(s) issued")
        print("Available copies =", self.get_copies())

    def return_book(self, count):
        self.copies += count
        print(count, "book(s) returned")
        print("Available copies =", self.get_copies())

    def get_copies(self):
        return self.copies


b1 = Library("Python", 10)
b1.issue(2)
b1.return_book(1)
b1.issue(3)