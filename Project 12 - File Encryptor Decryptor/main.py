from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    
    k_file = input("Enter file to save key : ")
    with open(f"{k_file}.key", 'wb') as key_file:
        key_file.write(key)
        print(f"Key saved Successfull at file : {k_file}.key")

def load_key():
    key_file = input("Enter the key file Name to load key: " )
    return open(f'{key_file}.key', 'rb').read()
                
def encrypt_file(f_name):
    key = load_key()
    fernet = Fernet(key)

    with open(f'{f_name}', 'rb') as file:
        f_data = file.read()

    encrypted_data = fernet.encrypt(f_data)

    f_name = input("Enter the file to save Encrypted Data : ")
    with open(f'{f_name}.txt', 'wb') as file:
        file.write(encrypted_data)
        print(f"Data Encrypted Successfull at file : {f_name}")


def decrypt_file(f_name):
    key = load_key()
    fernet = Fernet(key)

    data = open(f"{f_name}", 'rb').read()

    decrypted_data = fernet.decrypt(data)

    n_file = input("Enter file name to save Decrypted Data : ")

    with open(f"{n_file}.txt", 'wb') as file:
        file.write(decrypted_data)
        print(f"Plan Text Data Saved at file : {n_file}.txt")

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