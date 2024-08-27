import os
import json
import encrypt_data as ed
import random


def load_passwords():
    if os.path.exists(ed.PASSWORD_FILE):
        with open(ed.PASSWORD_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_passwords(passwords):
    with open(ed.PASSWORD_FILE, "w") as file:
        json.dump(passwords, file)


def add_password(website, username, password):
    passwords = load_passwords()
    encrypted_password = ed.cipher.encrypt(password.encode()).decode()
    passwords[website] = {"username": username, "password": encrypted_password}
    save_passwords(passwords)
    print(f"Password for {website} added.")

def view_password():
    passwords = load_passwords()
    for website, creds in passwords.items():
        decrypted_password = ed.cipher.decrypt(creds['password'].encode()).decode()
        print(f"Website: {website}, Username: {creds['username']}, Password: {decrypted_password}")

def delete_password(website):
    passwords = load_passwords()
    if website in passwords:
        del passwords[website]
        save_passwords(passwords)
        print(f"Password for {website} deleted.")
    else:
        print(f"No password found for {website}.")

def password_generator(password_length, include_uppercase, include_numbers, include_specialcase):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    specialcase = "!@#$%^&*()-_=+?/"
    characters = lowercase

    if include_uppercase == 'y':
        characters += uppercase
    if include_numbers == 'y':
        characters += numbers
    if include_specialcase == 'y':
        characters += specialcase
    
    password = "".join(random.choice(characters) for _ in range(password_length))
    return password
