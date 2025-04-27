import socket
import json
import os
import time
import datetime

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("",6000))

peers = {}

print("Peer Discovery has been started. I am listening all the broadcasts...\n")

while True:
    try:
        print("Bekleniyor...")
        data,addr = sock.recvfrom(1024)
        print("Veri alındı:", addr)
        
        message = data.decode()
        info = json.loads(message)
        
        username = info["username"]
        ip = addr[0]
        timestamp = time.time()
        
        if ip not in peers:
            print(f"{username} ({ip}) is online ")

        peers[ip] = {
            "username" : username,
            "last_seen" : timestamp
        }
        
        with open("peers.json", "w") as f:
            json.dump(peers, f, indent=4)
    
    except Exception as e:
        print("There is an error...")
        continue