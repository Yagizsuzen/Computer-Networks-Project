import socket
import json
import os

while True:
    username = input("Please enter your username: ").strip()
    if username:
        break
    print("Username can not be blank!")

try:
    ip_address = socket.gethostbyname(socket.gethostname())
    
    if ip_address.startswith("127."):
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()

except Exception as e:
    print("IP address could not find.")
    ip_address = "0.0.0.0"

user_info = {
    "username" : username,
    "ip" : ip_address
}

with open("user_info.json","w") as f:
    json.dump(user_info,f, indent=4)

print("User info saved succesfully.")