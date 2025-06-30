"""
remove_session.py

This script deletes the existing Telethon session file used for authentication.

Use this when you want to:
- Reset the session
- Login using a different Telegram account
- Clear a corrupted or expired session

Steps:
1. Check if the session file exists
2. Ask for confirmation
3. Delete the session file if confirmed

Location of the session:
- ./session/user.session

⚠️ Warning: Deleting the session will require you to log in again the next time you run the bot.
"""

import os

# === Define absolute path to session file ===
session_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "session", "user.session"))

# === Check and confirm deletion ===
if os.path.exists(session_file):
    confirm = input(f"Are you sure you want to delete the session file?\n{session_file}\n(y/n): ").strip().lower()
    if confirm == 'y':
        os.remove(session_file)
        print("✅ Session file deleted.")
    else:
        print("❌ Operation cancelled.")
else:
    print("ℹ️ No session file found at:", session_file)
