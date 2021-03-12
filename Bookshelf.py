from Book import Book, Shelf


class Bookshelf:
    def __init__(self, shelf: dict = {}):
        self.shelf = {q: {} for q in ["WANT_TO_READ", "READING", "READ"]}

    def add_book(self, book: Book):
        _shelf = self.shelf[book.shelf.value]
        if book.author in _shelf.keys():
            _shelf[book.author].append(book)
        else:
            _shelf[book.author] = []
            self.add_book(book)

    def show(self):
        for k in self.shelf.keys():
            print(k)
            for v in self.shelf[k]:
                print(f"\t{v}")
                for _v in self.shelf[k][v]:
                    print(f"\t\t{_v}")
