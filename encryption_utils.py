# encryption_utils.py
from pyDes import triple_des, PAD_PKCS5
import base64
import os

def encrypt_message(key, message):
    cipher = triple_des(key, padmode=PAD_PKCS5)
    encrypted = cipher.encrypt(message.encode())
    return base64.b64encode(encrypted).decode()

def decrypt_message(key, encrypted_message):
    cipher = triple_des(key, padmode=PAD_PKCS5)
    decoded = base64.b64decode(encrypted_message)
    return cipher.decrypt(decoded).decode()

def diffie_hellman_generate_private_key():
    return int.from_bytes(os.urandom(2), "big") % 19

def diffie_hellman_generate_public_key(private_key, g=2, p=19):
    return pow(g, private_key, p)

def diffie_hellman_generate_shared_secret(other_public, private_key, p=19):
    return pow(other_public, private_key, p)
