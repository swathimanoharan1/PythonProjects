import book_management as bm
import file_handling as fh

def main():
    fh.load_books()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Display Books")
        print("7. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            bm.add_book(title, author)

        elif choice == '2':
            book_id = input("Enter book ID to remove: ")
            bm.remove_book(book_id)

        elif choice == '3':
            book_id = input("Enter book ID to issue: ")
            user = input("Enter user name: ")
            bm.issue_book(book_id, user)

        elif choice == '4':
            book_id = input("Enter book ID to return: ")
            user = input("Enter user name: ")
            bm.return_book(book_id, user)

        elif choice == '5':
            query = input("Enter title or author to search: ")
            results = bm.search_book(query)
            if results:
                for book in results:
                    print(f"Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")
            else:
                print("No books found.")

        elif choice == '6':
            bm.display_books()

        elif choice == '7':
            fh.save_books()
            print("Changes saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
