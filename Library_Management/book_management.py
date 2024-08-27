import file_handling as fh


def add_book(title, author):
    fh.current_book_id += 1
    book_id = str(fh.current_book_id)
    fh.books[book_id] = {'title': title, 'author': author, 'status': 'available'}
    print(f"Book '{title}' added successfully!")


def remove_book(book_id):
    if book_id in fh.books:
        del fh.books[book_id]
        print("Book removed successfully!")
    else:
        print("Book not found.")


def issue_book(book_id, user):
    if book_id in fh.books and fh.books[book_id]['status'] == 'available':
        fh.books[book_id]['status'] = f"Book issued to {user}"
        print(f"Book '{fh.books[book_id]['title']}' issued to {user}.")
        fh.log_user_action(user, book_id, fh.books[book_id]['title'], 'Issued')
    else:
        print("Book is not available.")


def return_book(book_id, user):
    if book_id in fh.books and "issued" in fh.books[book_id]['status']:
        fh.books[book_id]['status'] = 'available'
        print(f"Book '{fh.books[book_id]['title']}' returned successfully!")
        fh.log_user_action(user, book_id, fh.books[book_id]['title'], 'Returned')
    else:
        print("Book not found or not issued.")


def search_book(query):
    found_books = [details for details in fh.books.values()
                   if query.lower() in details['title'].lower() or query.lower() in details['author'].lower()]
    return found_books


def display_books():
    if fh.books:
        for book_id, details in fh.books.items():
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Status: {details['status']}")
    else:
        print("No books available.")
