import socket
import json
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 6000))
sock.settimeout(2)

try:
    with open("peers.json", "r") as f:
        peers = json.load(f)
except:
    peers = {}

print("Peer Discovery started, listening for broadcasts...")

while True:
    try:
        data, addr = sock.recvfrom(1024)
        message = json.loads(data.decode())
        username = message["username"]
        ip = addr[0]
        timestamp = time.time()

        if ip in peers:
            peers[ip]["last_seen"] = timestamp
        else:
            peers[ip] = {"username": username, "last_seen": timestamp}
            print(f"{username} ({ip}) is online!")

        with open("peers.json", "w") as f:
            json.dump(peers, f, indent=4)

    except socket.timeout:
        continue
    except Exception as e:
        print(f"Error: {e}")
