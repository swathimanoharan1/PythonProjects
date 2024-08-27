books = {}

def generate_book_id():
    return str(len(books) + 1)

def add_book(book_id, title, author):
    books[book_id] = {'title': title, 'author': author, 'status': 'available'}

def remove_book(book_id):
    if book_id in books:
        del books[book_id]

def issue_book(book_id, user):
    if book_id in books:
        books[book_id]['status'] = f'Issued to {user}'

def return_book(book_id, user):
    if book_id in books:
        books[book_id]['status'] = 'available'

def search_book(query):
    return [book for book in books.values() if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]

def display_books():
    return books
