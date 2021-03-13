from typer import Argument, Typer, Option, echo
from typing import Optional
from Bookshelf import Bookshelf
from Book import Book
from FileHandler import FileHandler
import os

bookstack = Bookshelf()
cli = Typer()


@cli.command()
def add_book(
    from_csv: bool = Option(
        default=False,
        prompt="Would you like to add multiple books using a CSV file?",
        help="Add multiple books using a CSV file.",
    ),
) -> None:
    if from_csv:
        path = input("Enter the path of the CSV file you'd like to use: ")

        assert os.path.exists(path), "File not found at %s" % path

        file_handler = FileHandler(path)
        rows = file_handler.open()
        [bookstack.add_book(book) for book in [Book.from_str(row) for row in rows]]


@cli.command()
def show() -> None:
    echo(bookstack.show())


@cli.command()
def init() -> None:

    path = os.path.join(os.getenv("HOME") + "/" + ".bookstacks")

    os.mkdir(path)


@cli.command()
def uninit() -> None:
    path = os.path.join(os.getenv("HOME") + "/" + ".bookstacks")
    os.rmdir(path)


if __name__ == "__main__":
    cli()
