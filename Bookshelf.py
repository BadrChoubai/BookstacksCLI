from Book import Book, Shelf
from collections import defaultdict
from Book import Shelf
from pprint import pprint


class Bookshelf:
    def __init__(self, shelf: dict = {}) -> object:
        self.shelf = defaultdict(dict)
        for q_name in Shelf.list():
            self.shelf[q_name] = defaultdict(list)

    def add_book(self, book: Book) -> None:
        _shelf = self.shelf[book.shelf.value]
        _shelf[book.author].append(book)
        print(f"{book.title} by {book.author} add to shelf: {book.shelf}")

    def show(self) -> None:
        for k in self.shelf.keys():
            print(k)
            for v in self.shelf[k]:
                print(f"\t{v}")
                for _v in self.shelf[k][v]:
                    print(f"\t\t{_v}")
