from cryptography.fernet import Fernet 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def load_key(password):
    # The salt is a predefined value used for salting the input.
    # Salting helps prevent rainbow table attacks.
    salt = b'\xaa\xf1\xa2\x04\xe9\xa9Z\xfb\xb1\xb6}8\xf6\xa2'
    
    # Key derivation using PBKDF2HMAC with SHA256 hash function.
    # PBKDF2HMAC is a key derivation function (KDF) for password-based key derivation.
    # It iteratively applies a pseudorandom function to derive a key from the password and salt.
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # The length of the derived key is set to 32 bytes (256 bits).
        salt=salt,
        iterations=100000,  # Number of iterations of the hash function.
    )
    key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key)

def view(fer):
    # Read and decrypt passwords from the 'passwords.txt' file.
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            # Decrypt the password and print the user and password.
            print("User:", user, "|, Password:", fer.decrypt(passw.encode()).decode())

def add(fer):
    # Prompt the user to input the account name and password.
    name = input("Account name: ")
    pwd = input("Password: ")

    # Append the encrypted account name and password to the 'passwords.txt' file.
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def main():
    # Get the master password from the user.
    master_pwd = input("What is the master password? ")

    # Load the key using the master password.
    key = load_key(master_pwd)
    
    # Create a Fernet instance with the derived key.
    fer = Fernet(key)

    # Main loop for interacting with the password manager.
    while True:
        mode = input("Would you like to add a new password or view existing ones?\nEnter 'add' to add a new password, 'view' to view existing passwords, or 'q' to quit: ")
        if mode.lower() == "q":
            break
        elif mode.lower() == "view":
            view(fer)
        elif mode.lower() == "add":
            add(fer)
        else:
            print("\nInvalid input. Please enter 'add', 'view', or 'q' to quit.\n")
    
    print("EOF. Goodbye!")

if __name__ == "__main__":
    main()
