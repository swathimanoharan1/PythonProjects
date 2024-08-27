import json
from book_management import books

def load_books():
    try:
        with open('books.json', 'r') as file:
            global books
            books.update(json.load(file))
    except FileNotFoundError:
        pass

def save_books():
    with open('books.json', 'w') as file:
        json.dump(books, file)
