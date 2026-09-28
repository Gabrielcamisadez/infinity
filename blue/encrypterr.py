from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def new_file(name):
    file = open(name, "w")
    file.write("teste")
    file.close()
    data = file

    return data


def crypt_file(name, data):
    encrypted = cipher.encrypt(data)

    file = open(name + ".enc", "wb")
    file.write(encrypted)
    file.close()

    print("Criptografado!")


def decrypt_file(name):
    file = open(name, "rb")
    data = file.read()
    file.close()

    decrypted = cipher.decrypt(data)

    file = open(name + ".dec", "wb")
    file.write(decrypted)
    file.close()

    print("Descriptografado!")


data = new_file("teste.txt")

crypt_file("teste.txt", data)

decrypt_file("teste.txt.enc")
