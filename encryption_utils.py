import base64
from pyDes import des, CBC, PAD_PKCS5
import os

# DES Encryption
def encrypt_message(key, message):
    cipher = des(key, CBC, key, pad=None, padmode=PAD_PKCS5)
    encrypted = cipher.encrypt(message)
    return base64.b64encode(encrypted).decode()

# DES Decryption
def decrypt_message(key, encrypted_message):
    cipher = des(key, CBC, key, pad=None, padmode=PAD_PKCS5)
    decoded = base64.b64decode(encrypted_message)
    return cipher.decrypt(decoded).decode()

# Diffie-Hellman
def diffie_hellman_generate_private_key():
    return int.from_bytes(os.urandom(2), "big") % 19

def diffie_hellman_generate_public_key(private_key, g=2, p=19):
    return pow(g, private_key, p)

def diffie_hellman_generate_shared_secret(other_public, private_key, p=19):
    return pow(other_public, private_key, p)
