import tkinter as tk
from tkinter import messagebox
import book_management as bm
import file_handling as fh

root = tk.Tk()
root.title("Library Management System")
root.geometry("600x400")

fh.load_books()

def add_book_ui():
    add_window = tk.Toplevel(root)
    add_window.title("Add Book")

    tk.Label(add_window, text='Title: ').pack(pady=5)
    title_entry = tk.Entry(add_window)
    title_entry.pack(pady=5)

    tk.Label(add_window, text='Author: ').pack(pady=5)
    author_entry = tk.Entry(add_window)
    author_entry.pack(pady=5)

    def submit_add():
        title = title_entry.get()
        author = author_entry.get()
        book_id = bm.generate_book_id()
        bm.add_book(book_id, title, author)
        messagebox.showinfo("Success", "Book added successfully")
        add_window.destroy()

    tk.Button(add_window, text="Add Book", command=submit_add).pack(pady=10)


def remove_book_ui():
    remove_window = tk.Toplevel(root)
    remove_window.title("Remove Book")

    tk.Label(remove_window, text='Book ID: ').pack(pady=5)
    book_id_entry = tk.Entry(remove_window)
    book_id_entry.pack(pady=5)

    def submit_remove():
        book_id = book_id_entry.get()
        bm.remove_book(book_id)
        messagebox.showinfo("Success", "Book removed successfully")
        remove_window.destroy()

    tk.Button(remove_window, text="Remove Book", command=submit_remove).pack(pady=10)


def issue_book_ui():
    issue_window = tk.Toplevel(root)
    issue_window.title("Issue Book")

    tk.Label(issue_window, text='Book ID: ').pack(pady=5)
    book_id_entry = tk.Entry(issue_window)
    book_id_entry.pack(pady=5)

    tk.Label(issue_window, text='User Name: ').pack(pady=5)
    user_entry = tk.Entry(issue_window)
    user_entry.pack(pady=5)

    def submit_issue():
        book_id = book_id_entry.get()
        user = user_entry.get()
        bm.issue_book(book_id, user)
        messagebox.showinfo("Success", "Book issued successfully")
        issue_window.destroy()

    tk.Button(issue_window, text="Issue Book", command=submit_issue).pack(pady=10)


def return_book_ui():
    return_window = tk.Toplevel(root)
    return_window.title("Return Book")

    tk.Label(return_window, text='Book ID: ').pack(pady=5)
    book_id_entry = tk.Entry(return_window)
    book_id_entry.pack(pady=5)

    tk.Label(return_window, text='User Name: ').pack(pady=5)
    user_entry = tk.Entry(return_window)
    user_entry.pack(pady=5)

    def submit_return():
        book_id = book_id_entry.get()
        user = user_entry.get()
        bm.return_book(book_id, user)
        messagebox.showinfo("Success", "Book returned successfully")
        return_window.destroy()

    tk.Button(return_window, text="Return Book", command=submit_return).pack(pady=10)


def search_book_ui():
    search_window = tk.Toplevel(root)
    search_window.title("Search Book")

    tk.Label(search_window, text='Query (Title or Author): ').pack(pady=5)
    query_entry = tk.Entry(search_window)
    query_entry.pack(pady=5)

    def submit_search():
        query = query_entry.get()
        results = bm.search_book(query)
        
        if results:
            result_window = tk.Toplevel(search_window)
            result_window.title("Search Results")
            for book in results:
                tk.Label(result_window, text=f"Title: {book['title']}, Author: {book['author']}, Status: {book['status']}").pack(pady=2)
        else:
            messagebox.showinfo("No Results", "No books found matching the query.")

        search_window.destroy()

    tk.Button(search_window, text="Search Book", command=submit_search).pack(pady=10)
    

def display_books_ui():
    display_window = tk.Toplevel(root)
    display_window.title("All Books")

    books = bm.display_books()
    for book_id, details in books.items():
        tk.Label(display_window, text=f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Status: {details['status']}").pack(pady=2)


def save_and_exit():
    fh.save_books()
    root.quit()

tk.Button(root, text="Add Book", command=add_book_ui).pack(pady=10)
tk.Button(root, text="Remove Book", command=remove_book_ui).pack(pady=10)
tk.Button(root, text="Issue Book", command=issue_book_ui).pack(pady=10)
tk.Button(root, text="Return Book", command=return_book_ui).pack(pady=10)
tk.Button(root, text="Search Book", command=search_book_ui).pack(pady=10)
tk.Button(root, text="Display Books", command=display_books_ui).pack(pady=10)
tk.Button(root, text="Save and Exit", command=save_and_exit).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
