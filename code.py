# 1.Install pycryptodome using pip:

# pip install pycryptodome

#2. Import the necessary modules in your Python script:
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from pathlib import Path

# 3.Define a function that takes a file path and a passphrase as arguments and encrypts the file:
def encrypt_file(file_path, passphrase):
    # generate a random salt
    salt = get_random_bytes(16)
    # use the passphrase and salt to derive a key and initialization vector
    key, iv = derive_key_and_iv(passphrase, salt)
    # create a new AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # read the contents of the file
    with open(file_path, "rb") as file:
        plaintext = file.read()
    # encrypt the plaintext and add the salt as a prefix
    ciphertext = salt + cipher.encrypt(pad(plaintext))
    # write the ciphertext back to the file
    with open(file_path, "wb") as file:
        file.write(ciphertext)

# 4.Use the os library to loop through all files in a specified directory and its subdirectories, and call the encrypt_file function on each file:
import os

root_directory = 'path/to/directory'
passphrase = "secret passphrase"

for dirpath, dirnames, filenames in os.walk(root_directory):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        encrypt_file(file_path, passphrase)


# 4.Test the program thoroughly to ensure that it encrypts all files correctly and that the encryption can be successfully decrypted with the correct passphrase.

# 5.Finally, make sure to store the passphrase securely, and backup the encrypted files in case the original files are lost or damaged.

# It's important to test this encryption on a test environment and not in production as it may cause irreparable damage to the data.
#  Also, make sure to follow the regulations and laws of your company and country related to data encryption and storage.