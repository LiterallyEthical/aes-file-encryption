from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import argparse

def encrypt_file(file_path, key_path):

    #Input Validation
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File could not found: " + file_path)

    if os.path.dirname(key_path) and not os.path.exists(os.path.dirname(key_path)):
        raise FileNotFoundError("File could not found: " + key_path)
        
    # Generates a random key
    key = get_random_bytes(16)

    # Encrypting the file
    cipher = AES.new(key, AES.MODE_EAX)
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # Writes the encrypted file
    with open(file_path + ".aes", 'wb') as f:
        [f.write(x) for x in (cipher.nonce, tag, ciphertext)]

    # Writes the key to a separate file
    with open(key_path, 'wb') as f:
        f.write(key)

    # Deletes the original file
    try:
        os.remove(file_path)
        print("Original file deleted")

    except:
        print("Original file could not deleted.")

def decrypt_file(file_path, key_path):

    #Input Validation
    if os.path.dirname(file_path) and not os.path.exists(os.path.dirname(file_path)):
        raise FileNotFoundError("File could not found: " + file_path)    

    if not os.path.isfile(key_path):
        raise FileNotFoundError("File could not found: " + key_path)    

    # Read the key from file
    with open(key_path, 'rb') as f:
        key = f.read()

    # Decrypt the file
    with open(file_path, 'rb') as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    # Write the decrypted file
    with open(file_path[:-4], 'wb') as f:
        f.write(plaintext)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A simple command line tool that encrypts and decrypts files using AES encryption and stores the key in a separate file.")    
    parser.add_argument('file_path', type=str, help="File path to encrypt or decyrpt")
    parser.add_argument('key_path', type=str, help="File path to save the key or read the key")
    parser.add_argument('-d', '--decrypt', action='store_true',help="Option that switchs to decyrpt mode, default is encyrpt")

    args = parser.parse_args()
    if args.decrypt:
        decrypt_file(args.file_path, args.key_path)
    else:
        encrypt_file(args.file_path, args.key_path)
