class Library:

    books = {}
    readers = []

    min_price = 0
    max_price = 0

    def __init__(self, name):
        self.name = name

    def add_book(self, book):
        Library.books.update(book)

        for name, price in Library.books.items():
            if price < Library.min_price or Library.min_price == 0: Library.min_price = price
            if price > Library.max_price: Library.max_price = price

    def add_reader(self, reader):
        Library.readers.append(reader)



class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return 'That`s a person`s class'


class Programmer(Person):
    def __init__(self, programming_language, *args):
        super().__init__(*args)
        self.programming_language = programming_language

    def __str__(self):
        return 'I am {} {} and my favorite programming language is {}!'.format(self.name, self.surname, self.programming_language)


library = Library("Library")

library.add_book({'1': 10})
library.add_book({'2': 40})
library.add_book({'3': 30})
library.add_book({'4': 20})

programmer1 = Programmer('Java Script', 'Mathew', 'Rainy')
programmer2 = Programmer('Python', 'Bob', 'Nicolshon')

library.add_reader(programmer1.__str__())
library.add_reader(programmer2.__str__())

print(library.name, library.books, library.readers, library.min_price, library.max_price)
print(programmer1.programming_language, programmer1.name, programmer1.surname)
print(programmer2.programming_language, programmer2.name, programmer2.surname)