"""
man_addG.py

This script allows a user to add a group to the bot system by sending
a "/addgroup <group_id>" command to a specified Telegram thread.

Steps:
1. Prompt user to input a group ID (numbers only)
2. Send the /addgroup command to the group/topic
3. Wait for a bot response
4. If no response is detected, fallback to triggering /start

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

# === 1. Ask user to enter target group ID ===
user_input = input("Enter group ID (only numbers): ").strip()

if not user_input.isdigit():
    print("❌ Invalid input: must be numbers only.")
    sys.exit(1)

# === 2. Format the command ===
command = f"/addgrup {user_input}"

# === 3. Send command to Telegram ===
with TelegramClient(session_path, api_id, api_hash) as client:
    client.send_message(group_id, command, reply_to=topic_id)
    print(f"📨 Sent command: {command}")
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

# === 4. Run /start automatically if no bot response ===
if should_trigger_start:
    print("🚀 Running /start as fallback...")
    run_start()
