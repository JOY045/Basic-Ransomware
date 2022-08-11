import os

from cryptography.fernet import Fernet

KEY = input('Please Enter the Key: ')

fernet = Fernet(KEY)


def decrypt(file):
    try:
        with open(file, 'rb') as myFile:
            myFileData = myFile.read()

        decryptedMyFileData = fernet.decrypt(myFileData)

        with open(file, 'wb') as myFile:
            myFile.write(decryptedMyFileData)

    # except InvalidToken:
    #     print('Invalid Token')
    #     exit()

    except Exception:
        return


for file in os.listdir():
    # if file == 'encrypt.py' or file == 'key_file.key' or file == 'decrypt.py':
    if file in ['encrypt.py', 'key_file.key', 'decrypt.py']:
        continue
    elif os.path.isfile(file):
        decrypt(file)
