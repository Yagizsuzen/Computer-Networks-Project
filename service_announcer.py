import socket
import json
import time

with open("user_info.json", "r") as f:
    user_info = json.load(f)

username = user_info["username"]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

message = json.dumps({"username": username})

while True:
    sock.sendto(message.encode(), ("255.255.255.255", 6000))
    print(f"Broadcast sent: {username}")
    time.sleep(8)
