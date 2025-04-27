import json
import time
import os

if not os.path.exists("peers.json"):
    print("peers.json bulunamadı. Önce peer_discovery.py çalışmalı.")
    exit()

with open("peers.json", "r") as f:
    peers = json.load(f)

now = time.time()


for ip, info in peers.items():
    username = info["username"]
    last_seen = info["last_seen"]
    delta = now - last_seen


    if delta <= 10:
        status = "Online"
    elif delta <= 900:
        status = "Away"
    else:
        continue  


    print(f"{username} ({ip}) — {status}")

print("-" * 30)