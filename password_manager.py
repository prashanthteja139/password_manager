import os
from getpass import getpass
from utils import generate_key, load_key, encrypt_message, decrypt_message
import json
import secrets
import string

# Ensure the key file exists or generate a new key
if not os.path.exists("secret.key"):
    generate_key()

key = load_key()

# File to store passwords
PASSWORD_FILE = "passwords.json"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def save_password(service, password):
    encrypted_password = encrypt_message(password, key)
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            data = json.load(file)
    else:
        data = {}
    data[service] = encrypted_password.decode()
    with open(PASSWORD_FILE, "w") as file:
        json.dump(data, file)

def get_password(service):
    if not os.path.exists(PASSWORD_FILE):
        print("No passwords saved yet.")
        return None
    with open(PASSWORD_FILE, "r") as file:
        data = json.load(file)
    encrypted_password = data.get(service)
    if encrypted_password:
        decrypted_password = decrypt_message(encrypted_password.encode(), key)
        return decrypted_password
    else:
        print(f"No password found for {service}.")
        return None

def main():
    while True:
        print("\nPassword Manager")
        print("1. Save Password")
        print("2. Retrieve Password")
        print("3. Generate Password")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            service = input("Enter the service name: ")
            password = getpass("Enter the password: ")
            save_password(service, password)
            print("Password saved successfully.")

        elif choice == "2":
            service = input("Enter the service name: ")
            password = get_password(service)
            if password:
                print(f"The password for {service} is: {password}")

        elif choice == "3":
            length = int(input("Enter the desired password length: "))
            print(f"Generated password: {generate_password(length)}")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
