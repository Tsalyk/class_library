class Library:

    def __init__(self, list_books, list_readers):
        self.books = list_books
        self.readers = list_readers


    def add_book(self, book):
        self.books.append(book)


    def remove_book(self, book):
        self.books.remove(book)


    def give_book(self, book, reader):
        for index, el in enumerate(self.readers):
            if el[0] == reader:
                ind = index

        self.remove_book(book)
        self.readers[ind] = self.readers[ind], book


    def get_book(self, book, reader):
        for index, el in enumerate(self.readers):
            if el[0] == reader:
                ind = index

        self.books.append(book)
        self.readers[ind] = self.readers[ind][0]


    def available_books(self):
        print(self.books)


    def not_available_books(self):
        self.not_availabale_lst = list(filter(lambda el: len(el) == 2,
                                              self.readers))
        self.not_availabale_lst = list(map(lambda el: el[1],
                                           self.not_availabale_lst))

        print(self.not_availabale_lst)


    def sort_books_by_title(self, books):
        pass


    def sort_books_by_author(self, books):
        pass


    def sort_books_by_year(self, books):
        pass


class Books:

    def __init__(self, book_id, book_title, book_author, book_year):
        self.id = book_id
        self.title = book_title
        self.author = book_author
        self.year = book_year





lib = Library(["Harry Potter", "Snow"], ["Mark"])

lib.give_book("Harry Potter", "Mark")
lib.not_available_books()
print(lib.readers)
lib.get_book("Harry Potter", "Mark")
lib.available_books()
lib.give_book("Snow", "Mark")
print(lib.readers)
lib.give_book("Harry Potter", "Mark")
lib.available_books()
