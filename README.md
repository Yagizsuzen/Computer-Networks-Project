#Peer-to-Peer Secure Chat Application

## Project Overview
This project is a Peer-to-Peer (P2P) chat application that operates within a Local Area Network (LAN).  
Users can discover each other and exchange both **encrypted** and **unencrypted** messages.

The application consists of 4 main components:
- **PeerDiscovery**: Listens for UDP broadcasts to discover users.
- **ServiceAnnouncer**: Periodically sends UDP broadcasts announcing the user's presence.
- **ChatInitiator**: Provides a menu interface for viewing users, initiating chat sessions, and viewing chat history.
- **ChatResponder**: Listens for incoming TCP connections and handles chat sessions.

## How to Run
1. **Requirements:**
   - Python 3
   - Install `pyDes` library (`pip install pyDes`)

2. **Setup:**
   - Place all project files in the same folder.
   - Run the user setup once to create `user_info.json` (to save your username).

3. **Running the Application:**
   - Start Peer Discovery: `python PeerDiscovery.py`
   - Start Service Announcer: `python ServiceAnnouncer.py`
   - Start ChatResponder: `python ChatResponder.py`
   - Start ChatInitiator: `python ChatInitiator.py`
   
   *(Each script should run in a separate terminal window.)*

4. **Functional Features:**
   - Displays users discovered within the last 15 minutes.
   - Shows users as **Online** if they sent a broadcast within the last 10 seconds, otherwise shows them as **Away**.
   - Supports both **secure (encrypted)** and **unsecure** messaging modes.
   - Logs all messages in `chat_log.txt` with timestamp, username, and whether the message was SENT or RECEIVED.

5. **Sample Usage:**
   - View user list: Choose "Users" from the menu.
   - Initiate a chat: Choose "Chat" from the menu, select a username, and choose secure or unsecure communication.
   - View chat history: Choose "History" from the menu.

## Known Limitations
- Works only inside the same LAN; it does not support communication over the internet.
- Diffie-Hellman key exchange uses fixed parameters (p=19, g=2).
- TCP connection errors must be handled manually (restart chat session if disconnected).

## Developers
- Team 200tl
- Ata Berker Özer
- Yağız Süzen
- Efe Günaydın
