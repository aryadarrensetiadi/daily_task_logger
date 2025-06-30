"""
task_logger.py

Main script to:
1. Join a Telegram group using a given group ID.
2. Send a list of task messages (from a log file) to a specified topic in the group.
3. Trigger a collaboration summary function.

Dependencies:
- Telethon
- Local modules: config, man_joinG, man_collab

Make sure you have a valid log file and configured credentials in config.py
"""

import os
import sys
import time
from telethon.sync import TelegramClient

# Add 'actions' directory to the module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "actions")))

# Load configuration and local functions
from config import api_id, api_hash, group_id, topic_id, log_path, session_path
from man_joinG import run_join_group
from man_collab import run_collab

# === Step 1: Ask user for group ID (used by join and collab functions) ===
shared_input = input("Enter group ID (only numbers): ").strip()

# === Step 2: Join the specified group ===
run_join_group(shared_input)

# === Step 3: Send each line in log file as a "/add" command to the group ===
with TelegramClient(session_path, api_id, api_hash) as client:
    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line:
                message = f"/add {line}"
                client.send_message(entity=group_id, message=message, reply_to=topic_id)
                time.sleep(0.5)  # avoid flooding

# === Step 4: Run collaboration function to display all jobs ===
run_collab(shared_input)
