import json
import os
import socket
import time


with open("user_info.json","r") as f:
    user_info = json.load(f)
username = user_info["username"]

message = json.dumps({"username": username})

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    sock.sendto(message.encode(), ("192.168.1.255",6000))
    print("Broadcast sent: ",message)
    time.sleep(8)