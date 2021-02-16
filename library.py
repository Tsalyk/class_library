class Book:

    def __init__(self, book_id, title, author, year, reader_id):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.reader_id = reader_id


class People:

    def __init__(self, name, surname, age, books, my_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.books = books
        self.id = my_id


class Library:

    def __init__(self, list_books, list_readers):
        self.books = list_books
        self.readers = list_readers


    def add_book(self, book_id, title, author, year, reader_id):
        self.books.append(Book(book_id, title, author, year, reader_id))


    def remove_book(self, book_id):
        self.books = list(filter(lambda el: el.book_id != book_id, self.books))


    def give_book(self, book_id, reader_id):
        for ind, el in enumerate(self.books):
            if el.book_id == book_id:
                self.books[ind].reader_id = reader_id

                for subind, subel in enumerate(self.readers):
                    if subel.id == reader_id:
                        if self.readers[subind].books != None:
                            self.readers[subind].books.append(el.title)
                        else:
                            self.readers[subind].books = [el.title]


    def get_book(self, book_id, reader_id):
        for ind, el in enumerate(self.books):
            if el.book_id == book_id:
                self.books[ind].reader_id = None

                for subind, subel in enumerate(self.readers):
                        if subel.id == reader_id:
                            self.readers[subind].books.remove(el.title)

    def all_books(self):
        return list(map(lambda el: el.title, self.books))


    def available_books(self):
        available_books =  list(filter(lambda el: el.reader_id == None,
                                        self.books))
        return list(map(lambda el: el.title, available_books))


    def not_available_books(self):
        available_books =  list(filter(lambda el: el.reader_id != None,
                                        self.books))
        return list(map(lambda el: el.title, available_books))


    def sort_books_by_title(self):
        sorted_books = sorted(self.books, key=lambda el: el.title)
        return list(map(lambda el: el.title, sorted_books))


    def sort_books_by_author(self):
        sorted_books = sorted(self.books, key=lambda el: el.author)
        return list(map(lambda el: el.title, sorted_books))


    def sort_books_by_year(self):
        sorted_books = sorted(self.books, key=lambda el: el.year)
        return list(map(lambda el: el.title, sorted_books))
