from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Shelf(ExtendedEnum):
    WANT_TO_READ = "WANT_TO_READ"
    READING = "READING"
    READ = "READ"


class Book:
    def __init__(self, author: str, title: str, shelf: str = "WANT_TO_READ"):
        self.author = author
        self.title = title
        self.shelf = Shelf(shelf)

    @classmethod
    def from_str(cls, details: list):
        return cls(*details)

    def __repr__(self):
        return "Book(author=%s, title=%s, shelf?=%s)" % (
            self.author,
            self.title,
            self.shelf,
        )
