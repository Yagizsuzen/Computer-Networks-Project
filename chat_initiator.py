import socket
import json
import time
from encryption_utils import encrypt_message, diffie_hellman_generate_private_key, diffie_hellman_generate_public_key, diffie_hellman_generate_shared_secret
import os

def log_message(direction, username, message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("chat_log.txt", "a") as f:
        f.write(f"{timestamp} - {direction} - {username}: {message}\n")

def load_peers():
    try:
        with open("peers.json", "r") as f:
            return json.load(f)
    except:
        return {}

def display_users():
    peers = load_peers()
    now = time.time()
    for ip, info in peers.items():
        last_seen = now - info["last_seen"]
        status = "Online" if last_seen <= 900 else "Away"
        print(f"{info['username']} ({ip}) - {status}")


def initiate_chat():
    peers = load_peers()
    target_username = input("Kiminle konuşmak istiyorsun?: ").strip()

    target_ip = None
    for ip, info in peers.items():
        if info["username"] == target_username:
            target_ip = ip
            break

    if not target_ip:
        print("Kullanıcı bulunamadı.")
        return

    secure = input("Secure chat mi? (e/h): ").strip().lower() == "e"

    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((target_ip, 6001))
    except:
        print("Bağlantı kurulamadı.")
        return   

    if secure:
        try:
            user_input = input("Lütfen bir integer key girin: ").strip()
            private_key = int(user_input)
            public_key = diffie_hellman_generate_public_key(private_key)

            conn.send(json.dumps({"key": str(public_key)}).encode())

            data = conn.recv(4096)
            message_info = json.loads(data.decode())
            received_key = int(message_info["key"])

            shared_secret = diffie_hellman_generate_shared_secret(received_key, private_key)
            shared_key = (str(shared_secret).zfill(8))[:8].encode()
            print("Güvenli bağlantı kuruldu.")
        except Exception as e:
            print("Anahtar kurulum hatası:", e)
            return

    message = input("Mesajın: ")

    if secure:
        encrypted = encryptmessage(shared_key, message)
        conn.send(json.dumps({"encrypted_message": encrypted}).encode())
    else:
        conn.send(json.dumps({"unencrypted_message": message}).encode())

    log_message("SENT ", target_ip, message)
    conn.close()

def display_history():
    if not os.path.exists("chat_log.txt"):
        print("Hiç kayıt yok.")
        return

    with open("chat_log.txt", "r") as f:
        print(f.read())

while True:
    print("\nSeçenekler:\n1. Users\n2. Chat\n3. History\n4. Exit")
    choice = input("Seçiminiz: ").strip()

    if choice == "1":
        display_users()
    elif choice == "2":
        initiate_chat()
    elif choice == "3":
        display_history()
    elif choice == "4":
        break
    else:
        print("Geçersiz seçim.")
