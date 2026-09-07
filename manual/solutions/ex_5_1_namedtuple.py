# Create a namedtuple Book with the following fields: title, author, genre,
# pages, publisher. Create a Book object and try out some of the namedtuple
# operations presented above on it.
import csv
from collections import namedtuple
from pathlib import Path


Book = namedtuple("Book", "title, author, genre, pages, publisher")
my_book = Book("Brave New World", "Huxley, Aldous", "fiction", 311, "")
print(my_book.genre, my_book.pages)
print(my_book._asdict())

# Use the namedtuple to read rows from books.csv into Book records. Iterate on
# all books and display the name and author of books in computer_science genre.
books_path = Path.cwd().parent / "docs" / "books.csv"
with books_path.open() as f:
    reader = csv.reader(f)
    for book in map(Book._make, reader):
        if book.genre == "computer_science":
            print(f"\"{book.title}\" by {book.author}")
