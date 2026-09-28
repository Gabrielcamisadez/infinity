from cryptography.fernet import Fernet
import sys

key = Fernet.generate_key()
cipher = Fernet(key)

file_name = str(sys.argv[1]) if len(sys.argv) > 1 else "arquivo"

def new_file(name):
    full_name = f"{file_name}.txt"

    with open(full_name, "w", encoding="utf-8") as file:
        file.write("hello world")

    return full_name

def crypt_file(full_name):
    with open(full_name, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(full_name,  "wb") as file:
        file.write(encrypted_data)

    print(f"Arquivo {full_name} foi criptografado!! ")
    print(f"Chave de descriptografia: {key.decode()}")

created_file = new_file(file_name)
crypt_file(created_file)
    

