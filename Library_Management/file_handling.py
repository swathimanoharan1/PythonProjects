import csv
from datetime import datetime

books = {}
current_book_id = 0

def load_books(filename="data/books.csv"):
    global books, current_book_id
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books[row['ID']] = { 'title': row['Title'], 'author': row['Author'], 'status': row['Status']}
            if books:
                current_book_id = max(int(id) for id in books.keys())
    except FileNotFoundError:
        print("No existing book records found.")

def save_books(filename='data/books.csv'): 
    global books
    with open(filename, mode='w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=['ID', "Title", "Author","Status"])
        writer.writeheader()
        for book_id, details in books.items():
            writer.writerow({ 'ID': book_id, 'Title': details['title'], 'Author': details['author'], 'Status': details['status']})

def log_user_action(user, book_id, book_title, action, filename="data/users.csv"):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user, book_id, book_title, action, datetime.now().strftime("%d-%m-%Y %H:%M:%S")])
