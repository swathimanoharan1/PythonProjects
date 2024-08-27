# encrypt_data.py
from cryptography.fernet import Fernet
import os
import json

KEY_FILE = "key.key"
PASSWORD_FILE = "data/passwords.json"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            try:
                return json.load(key_file)
            except json.JSONDecodeError:
                return {}
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

cipher = load_key()
