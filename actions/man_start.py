"""
man_start.py

This script sends the "/start" command to the Telegram group/topic
to initialize or wake up the bot manually or as a fallback from other scripts.

Steps:
1. Send the /start command to the group/topic
2. Used as a standalone script or utility from other modules

Dependencies:
- Telethon
- Local modules: config
"""

import os
import sys
from telethon.sync import TelegramClient

# Add root directory to sys.path for config import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import api_id, api_hash, group_id, topic_id, session_path

# === Function to send /start command ===
def run_start():
    with TelegramClient(session_path, api_id, api_hash) as client:
        client.send_message(group_id, "/start", reply_to=topic_id)
        print("📨 Sent command: /start")

# === Allow manual execution ===
if __name__ == "__main__":
    run_start()
