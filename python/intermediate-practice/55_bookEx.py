import book as b

br = b.BookRepository()

br.registerBook(b.Book('python', 20000, '12345678'))
br.registerBook(b.Book('java', 25000, '09876543'))
br.registerBook(b.Book('c/c++', 27000, '23456789'))

br.printBooksInfo()

print()

br.printBookInfo('09876543')
br.printBookInfo('12345678')

br.removeBook('12345678')

print()

br.printBooksInfo()

