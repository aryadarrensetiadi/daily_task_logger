"""
topicID_finder.py

Utility script to listen for incoming messages and extract:
- Telegram group/chat ID (event.chat_id)
- Thread/topic ID (event.message.reply_to_msg_id)
- Message content (event.message.message)

How to use:
1. Run this script with `python3 topicID_finder.py`
2. Send a message from your account to the target group/thread
3. The script will print the chat ID and topic ID to use in config.py

Note:
- Ensure your account is already part of the group you're testing.
- You must have a valid session_path set in config.py
"""

from telethon.sync import TelegramClient, events
from config import api_id, api_hash, session_path

# === Start a Telethon client to listen for messages ===
with TelegramClient(session_path, api_id, api_hash) as client:
    @client.on(events.NewMessage)
    async def handler(event):
        print("Chat ID:", event.chat_id)
        print("Message thread ID (topic):", event.message.reply_to_msg_id)
        print("Message text:", event.message.message)

    print("📡 Listening... Please send a message to the target group or topic.")
    client.run_until_disconnected()
