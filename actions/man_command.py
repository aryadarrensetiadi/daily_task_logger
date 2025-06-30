"""
man_command.py

This script provides an interactive command-line interface
to send custom bot commands directly to a Telegram group/topic.

It allows flexible testing and exploration of available commands
without modifying the source code for each one.

Usage:
- Run this script
- Type a command name (without the leading slash)
  Example: dump, result, collab, start
- Type 'q', 'exit', or 'quit' to leave the interface

Steps:
1. Prompt user to enter a custom command
2. Send the command to the group/topic
3. Wait for bot response
4. Show the response or fallback notice

Dependencies:
- Telethon
- Local modules: config
"""

import os
import sys
import time
from telethon.sync import TelegramClient

# Add root directory to sys.path for config import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import api_id, api_hash, group_id, topic_id, session_path

# === Manual command entry interface ===
def run_command():
    with TelegramClient(session_path, api_id, api_hash) as client:
        print("🧪 Manual command interface ready")
        print("ℹ️ Type command name without '/'. Example: dump, result, start")
        print("❌ Type 'q', 'exit', or 'quit' to leave.")

        while True:
            cmd = input("\n>> Command: /").strip()

            if cmd.lower() in ["exit", "quit", "q"]:
                print("👋 Exiting the program.")
                break

            if not cmd:
                continue

            # === Format and send the command ===
            full_command = f"/{cmd}"
            client.send_message(group_id, full_command, reply_to=topic_id)
            print(f"📨 Sent command: {full_command}")
            print("⏳ Waiting for response...")

            time.sleep(4)

            # === Fetch last 2 responses in thread ===
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
                print("   Try checking with the /start command.")

# === Allow direct execution ===
if __name__ == "__main__":
    run_command()
