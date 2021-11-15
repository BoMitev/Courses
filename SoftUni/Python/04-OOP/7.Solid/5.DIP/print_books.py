class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content


class UppercaseFormatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content.upper()


class Printer:
    @staticmethod
    def get_book(content):
        return content


book_name = Book("This is book content!")
formater = Formatter()
uppercase = UppercaseFormatter()
printer = Printer()

print(printer.get_book(formater.format(book_name)))
print(printer.get_book(uppercase.format(book_name)))
