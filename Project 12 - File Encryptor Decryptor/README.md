# File Encryptor and Decryptor

## Overview

The File Encryptor and Decryptor is a Python project that provides a simple yet secure way to encrypt and decrypt files. Using the `cryptography` library, this project allows users to generate a key, encrypt files with this key, and decrypt files using the same key. This ensures that sensitive data is protected from unauthorized access.

## Features

-   **Key Generation**: Generate a secure encryption key and save it to a file.
-   **File Encryption**: Encrypt any file and save the encrypted data to a new file.
-   **File Decryption**: Decrypt an encrypted file using the saved key and save the decrypted data to a new file.

## Prerequisites

Before you begin, ensure you have met the following requirements:

-   Python 3.x installed on your computer.
-   `cryptography` library installed. You can install it using pip:

bash

Copy code

`pip install cryptography` 

## Setup

1.  **Clone the repository:**

```
git clone https://github.com/JawadSher/Python-Projects-Beginner-to-Advance/tree/main/Project%2012%20-%20File%20Encryptor%20Decryptor
``` 

2.  **Navigate to the project directory:**


`cd File-Encryptor-Decryptor` 

3.  **Run the script:**


`python encryptor_decryptor.py` 

## Usage

### Generate a Key

1.  Run the script and choose option `1` to generate a key.
2.  Enter the desired filename to save the key (e.g., `mykey`).
3.  The key will be saved in a file named `mykey.key`.

### Encrypt a File

1.  Run the script and choose option `2` to encrypt a file.
2.  Enter the name of the file you wish to encrypt.
3.  Enter the name of the file to save the encrypted data (e.g., `encrypted_data`).
4.  The encrypted data will be saved in a file named `encrypted_data.txt`.

### Decrypt a File

1.  Run the script and choose option `3` to decrypt a file.
2.  Enter the name of the file you wish to decrypt.
3.  Enter the name of the file to save the decrypted data (e.g., `decrypted_data`).
4.  The decrypted data will be saved in a file named `decrypted_data.txt`.

### Exit

-   Choose option `4` to exit the script.

## Code Explanation

### Key Generation


```
def generate_key():
    key = Fernet.generate_key()
    k_file = input("Enter file to save key : ")
    with open(f"{k_file}.key", 'wb') as key_file:
        key_file.write(key)
        print(f"Key saved successfully at file: {k_file}.key")
``` 

-   Generates a key using `Fernet.generate_key()`.
-   Saves the key to a specified file.

### Load Key


```
def load_key():
    key_file = input("Enter the key file Name to load key: ")
    return open(f'{key_file}.key', 'rb').read()
``` 

-   Loads the key from a specified file.

### Encrypt File


```
def encrypt_file(f_name):
    key = load_key()
    fernet = Fernet(key)
    with open(f'{f_name}', 'rb') as file:
        f_data = file.read()
    encrypted_data = fernet.encrypt(f_data)
    f_name = input("Enter the file to save Encrypted Data : ")
    with open(f'{f_name}.txt', 'wb') as file:
        file.write(encrypted_data)
        print(f"Data Encrypted successfully at file: {f_name}")
``` 

-   Reads the file to be encrypted.
-   Encrypts the data using the loaded key.
-   Saves the encrypted data to a specified file.

### Decrypt File

```
def decrypt_file(f_name):
    key = load_key()
    fernet = Fernet(key)
    data = open(f"{f_name}", 'rb').read()
    decrypted_data = fernet.decrypt(data)
    n_file = input("Enter file name to save Decrypted Data : ")
    with open(f"{n_file}.txt", 'wb') as file:
        file.write(decrypted_data)
        print(f"Plain text data saved at file: {n_file}.txt")
``` 

-   Reads the encrypted file.
-   Decrypts the data using the loaded key.
-   Saves the decrypted data to a specified file.

### Main Menu

```
def main():
    print('------> Welcome to File Encryptor and Decryptor <------')
    print()
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")
    print()
    choice = input("Enter your choice : ")
    if choice == '1':
        generate_key()
    elif choice == '2':
        file_name = input("Enter the name of the file to encrypt: ")
        encrypt_file(file_name)
        print(f"{file_name} has been encrypted.")
    elif choice == '3':
        file_name = input("Enter the name of the file to decrypt: ")
        decrypt_file(file_name)
        print(f"{file_name} has been decrypted.")
    elif choice == '4':
        exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    while True:
        main()
``` 

-   Provides a menu for the user to choose an action.
-   Executes the chosen action.

## Execution Examples

### Example 1: Generate a Key

1.  **Run the script** and choose option `1` to generate a key:
    
    
    `python encryptor_decryptor.py` 
    
2.  **Select Option 1:**
    
    
    ```
    ------> Welcome to File Encryptor and Decryptor <------
    
    1. Generate Key
    2. Encrypt File
    3. Decrypt File
    4. Exit
    
    Enter your choice: 1
    ``` 
    
3.  **Enter the desired filename to save the key:**
    
    Copy code
    
    `Enter file to save key: mykey
    Key saved successfully at file: mykey.key` 
    

### Example 2: Encrypt a File

1.  **Run the script** and choose option `2` to encrypt a file:
    

    
    `python encryptor_decryptor.py` 
    
2.  **Select Option 2:**
    
    
     ```
    ------> Welcome to File Encryptor and Decryptor <------
    
    1. Generate Key
    2. Encrypt File
    3. Decrypt File
    4. Exit
    
    Enter your choice: 2
    ``` 
    
3.  **Enter the name of the file you wish to encrypt:**
    
    
    `Enter the name of the file to encrypt: plaintext.txt` 
    
4.  **Enter the name of the file to save the encrypted data:**
    
    
    ```
    Enter the file to save Encrypted Data: encrypted_data
    Data Encrypted successfully at file: encrypted_data
    ``` 
    

### Example 3: Decrypt a File

1.  **Run the script** and choose option `3` to decrypt a file:
    
    
    `python encryptor_decryptor.py` 
    
2.  **Select Option 3:**
    
    
    ```
    ------> Welcome to File Encryptor and Decryptor <------
    
    1. Generate Key
    2. Encrypt File
    3. Decrypt File
    4. Exit
    
    Enter your choice: 3
    ```  
    
3.  **Enter the name of the file you wish to decrypt:**
    
    `Enter the name of the file to decrypt: encrypted_data.txt` 
    
4.  **Enter the name of the file to save the decrypted data:**
    
    
    `Enter file name to save Decrypted Data: decrypted_data
    Plain text data saved at file: decrypted_data.txt` 
    

### Example 4: Exit the Script

1.  **Run the script** and choose option `4` to exit:
    
    
    `python encryptor_decryptor.py` 
    
2.  **Select Option 4:**
   
    
    ```
    ------> Welcome to File Encryptor and Decryptor <------
    
    1. Generate Key
    2. Encrypt File
    3. Decrypt File
    4. Exit
    
    Enter your choice: 4
    ``` 
    
3.  **Exit the script:**
   
    
    `Goodbye!`
