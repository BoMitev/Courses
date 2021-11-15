class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return "Successfully added the book"

    def find_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                return book


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.read_pages = 0

    def turn_page(self):
        self.read_pages += 1
        return self.read_pages

    def __str__(self):
        return f"{self.title} from {self.author}"
