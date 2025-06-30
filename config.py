"""
config.py

Configuration file for daily_task_logger.

This file contains all required credentials and paths used by the application.
Please make sure to replace placeholder values with your actual credentials.

Variables:
- api_id:       Telegram API ID (from https://my.telegram.org)
- api_hash:     Telegram API hash
- group_id:     Target Telegram group ID where messages will be sent
- topic_id:     Thread/topic ID inside the group (for threaded messages)
- log_path:     Path to the task log file (default: ./log.txt)
- session_path: Path to the saved Telethon session file
"""

import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# === Required Telegram credentials ===
api_id = YOUR_API_ID        # 🔧 Replace with your Telegram API ID
api_hash = 'YOUR_API_HASH'  # 🔧 Replace with your Telegram API hash

# === Telegram target destination ===
group_id = YOUR_GROUP_ID    # 🔧 Replace with the Telegram group ID
topic_id = YOUR_TOPIC_ID    # 🔧 Replace with the topic/thread ID in that group

# === Local file paths ===
log_path = os.path.join(BASE_DIR, "log.txt")                     # Task log file
session_path = os.path.join(BASE_DIR, "session/user.session")    # Telethon session file
