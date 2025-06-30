"""
man_listG.py

This script sends a "/listgroup" command to the Telegram group/topic
to request a list of all registered groups from the bot.

Steps:
1. Send the /listgroup command to the group/topic
2. Wait for a bot response
3. If no response is detected, fallback to triggering /start

Dependencies:
- Telethon
- Local modules: config, man_start
"""

import os
import sys
import time
from telethon.sync import TelegramClient

# Add root directory to sys.path for config & man_start import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import api_id, api_hash, group_id, topic_id, session_path
from man_start import run_start

# === Flag to trigger /start if needed ===
should_trigger_start = False

# === Send /listgroup command to Telegram ===
with TelegramClient(session_path, api_id, api_hash) as client:
    client.send_message(group_id, "/listgroup", reply_to=topic_id)
    print("📨 Sent command: /listgroup")
    print("⏳ Waiting for response...")

    time.sleep(5)

    # Fetch latest 2 messages in the thread to look for response
    messages = client.iter_messages(group_id, reply_to=topic_id, limit=2)

    has_response = False
    for msg in reversed(list(messages)):
        if msg.sender_id != client.get_me().id and msg.message:
            if not has_response:
                print("✅ Bot response:")
                has_response = True
            print(msg.text or msg.message)

    if not has_response:
        print("⚠️ No response detected. The bot might be offline.")
        should_trigger_start = True
        time.sleep(1)

# === Run /start automatically if no bot response ===
if should_trigger_start:
    print("🚀 Running /start as fallback...")
    run_start()
