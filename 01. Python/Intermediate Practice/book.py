class Book:
    def __init__(self, name, price, isbn):
        self.name = name
        self.price = price
        self.isbn = isbn

class BookRepository:
    def __init__(self):
        self.books = {}

    def registerBook(self, book):
        self.books[book.isbn] = book

    def removeBook(self, isbn):
        del self.books[isbn]

    def printBookInfo(self, isbn):
        if isbn in self.books.keys():
            book = self.books[isbn]
            print(f'name : {book.name}')
            print(f'price : {book.price}')
            print(f'isbn : {book.isbn}')
        else:
            print('Not Found!!')

    def printBooksInfo(self):
        for k in self.books.keys():
            self.printBookInfo(k)