import password_handler as ph

def main():
    while True:
        print("\nPassword Manager")
        print("1. Generate a Password")
        print("2. Add a Password")
        print("3. View Passwords")
        print("4. Delete a Password")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            password_length = int(input("Enter password length (numbers only): "))
            include_uppercase = input("Want to include uppercase letter? (y/n): ").lower()
            include_numbers = input("Want to include numbers? (y/n): ").lower()
            include_specialcase = input("Want to include special characters? (y/n): ").lower()

            generated_password = ph.password_generator(password_length, include_uppercase, include_numbers, include_specialcase)

            print("Generated password: ",generated_password)

            store_password = input("Would you like to save this password? (y/n): ").lower()
            if store_password == "y":
                website = input("Enter the website: ")
                username = input("Enter the username: ")
                ph.add_password(website, username, generated_password)
        
        elif(choice == '2'):
            website = input("Enter the website: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            ph.add_password(website, username, password)

        elif(choice == '3'):
            ph.view_password()

        elif(choice == '4'):
            website = input("Enter the website to delete: ")
            ph.delete_password(website)

        elif(choice == '5'):
            print("See you later!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

        