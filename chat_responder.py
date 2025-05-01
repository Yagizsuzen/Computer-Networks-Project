import socket
import json
import threading
import time
import os
from encryption_utils import decrypt_message, diffie_hellman_generate_private_key, diffie_hellman_generate_public_key, diffie_hellman_generate_shared_secret

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 6001))
server.listen()

print("ChatResponder is running...")

def log_message(direction, username, message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("chat_log.txt", "a") as f:
        f.write(f"{timestamp} - {direction} - {username}: {message}\n")

def handle_client(conn, addr):
    try:
        private_key = diffie_hellman_generate_private_key()
        public_key = diffie_hellman_generate_public_key(private_key)
        shared_key = None

        while True:
            data = conn.recv(4096)
            if not data:
                break

            try:
                message_info = json.loads(data.decode())

                if "key" in message_info:
                    received_key = int(message_info["key"])
                    shared_secret = diffie_hellman_generate_shared_secret(received_key, private_key)
                    conn.send(json.dumps({"key": public_key}).encode())
                    shared_key = (str(shared_secret).zfill(8))[:8].encode()
                    print(f"Secure channel established with {addr}")

                elif "encrypted_message" in message_info:
                    decrypted = decrypt_message(shared_key, message_info["encrypted_message"])
                    print(f"[Secure] {addr}: {decrypted}")
                    log_message("RECEIVED", addr[0], decrypted)

                elif "unencrypted_message" in message_info:
                    print(f"[Open] {addr}: {message_info['unencrypted_message']}")
                    log_message("RECEIVED", addr[0], message_info["unencryptedmessage"])

            except Exception as e:
                print(f"Error handling message: {e}")

    finally:
        conn.close()

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
