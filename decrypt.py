from cryptography.fernet import Fernet

def decryptFile(key_file, file_to_decrypt):
    with open(key_file,'rb') as file:
        key = file.read()

    f = Fernet(key)

    with open(file_to_decrypt,'rb') as encrypted_files:
        encrypted_file = encrypted_files.read()

    decrypted_file = f.decrypt(encrypted_file)
    try:
        with open(file_to_decrypt,'wb') as encrypted_files:
            encrypted_files.write(decrypted_file)
    except:
        print('ERROR')
    else:
        print("File was successfully decrypted.")

key_file = input("Enter decrypt key file path: ")
file_to_encrypt = input("Enter file to decrypt path: ")
decryptFile(key_file,file_to_encrypt)
