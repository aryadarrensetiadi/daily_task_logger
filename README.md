# 📋 Daily Task Logger

Automatically logs and sends your completed task entries to a Telegram group — built with Python and Telethon.

This tool was originally created to simplify personal productivity and task reporting. It can be run by regular users and provides both automatic logging and manual interaction features, including group and topic command tools.

---

## ✨ Features

- 🗒️ Automatically send daily task logs to Telegram
- 🧪 Send bot commands manually via interactive CLI
- 🔍 Retrieve group/topic/thread IDs
- 🧼 Manage session (clear/reset)
- 📦 Modular and extendable structure

---

## 📸 Screenshot

*Coming soon: Example log outputs and Telegram replies.*

---

## ⚙️ Requirements

- Python 3.6+
- Telegram `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org)
- Telegram account with access to the destination group/topic
- `telethon` library (installed automatically)

---

## 🚀 Installation

```bash
git clone https://github.com/aryadarrensetiadi/daily_task_logger.git
cd daily_task_logger
chmod +x install.sh
./install.sh
```
---

## 📁 Project Structure

```
daily_task_logger/
├── actions/                   # Manual command tools
│   ├── man_start.py             # Send /start command
│   ├── man_listG.py             # List all groups
│   ├── man_addG.py              # Add a group ID
│   ├── man_joinG.py             # Join a group by ID
│   ├── man_result.py            # Fetch result from bot
│   ├── man_collab.py            # Send /collab command
│   ├── man_dump.py              # Send /dump command
│   ├── man_command.py           # Interactive command shell
│   └── clear_session.py         # Delete saved session
│
├── session/                   # Telegram session data
│   └── user.session             # Created automatically after login
│
├── config.py                  # Configuration file (edit your credentials here)
├── install.sh                 # Setup script
├── log.txt                    # Your daily task entries
├── task_logger.py             # Main auto-logger script
├── topicID_finder.py          # Find group/topic IDs
├── README.md                  # This file
└── LICENSE                    # Open-source license
```

---

## 🧾 Usage

### 1. Get Your Credentials
Before using the app, you need to collect the following:
- `api_id` and `api_hash`
    - Visit [https://my.telegram.org](https://my.telegram.org)
    - Log in using your Telegram phone number
    - Go to API Development Tools
    - Fill in App title and Short name (can be anything)
    - For the website field, if you don’t have one, you can safely enter [http://localhost](http://localhost).
    - Copy the generated `api_id` and `api_hash`
- `group_id` and `topic_id`
    - Run the following script:
        ```bash
        python3 topicID_finder.py
        ```
    - Then, send a message to the Telegram group/topic where you want logs to appear.
    - Check your terminal output. It will look like:
        ```
        Chat ID: YOUR_GROUP_ID
        Message thread ID (topic): YOUR_TOPIC_ID
        Message text: Hello World!
        ```
    - Use the values for `group_id` and `topic_id`.

### 2. Set Your Credentials

Open `config.py` and fill in your credentials:

```python
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
group_id = YOUR_GROUP_ID
topic_id = YOUR_TOPIC_ID
```

### 3. Run Automatic Task Logger

Make sure `log.txt` contains your task list (one task per line).\
Then run:

```bash
python3 task_logger.py
```

It will automatically send tasks from `log.txt` to your configured Telegram group/topic.

### 4. Use Manual Command Tools

You can run specific commands using:

```bash
python3 actions/man_start.py       # Send /start
python3 actions/man_listG.py       # Get list of joined groups
python3 actions/man_addG.py        # Add a group ID
python3 actions/man_joinG.py       # Join a group
python3 actions/man_result.py      # Get result
python3 actions/man_collab.py      # Send /collab
python3 actions/man_dump.py        # Send /dump
python3 actions/man_command.py     # Interactive CLI for any command
```

### 5. Reset or Clear Session

```bash
python3 actions/clear_session.py
```

This deletes the Telegram session file if you need to re-login with a new account.

---

## 📄 License

This project is licensed under the **MIT License** — a simple and permissive license for open-source and commercial use.

See the [LICENSE](LICENSE) file for full text.

---

## 🤝 Contributions

Pull requests and feedback are welcome!

This is a lightweight project for productivity and personal use.\
Feel free to fork, improve, and share.

---

## 👤 Author

Made with ❤️ by **Arya Darren Setiadi**

- 📧 **Email:** [aryasetiadi@aripurin.my.id](mailto:aryasetiadi@aripurin.my.id)  
- 🌐 **Website:** [www.aripurin.my.id](https://www.aripurin.my.id) *(coming soon)*  
- 📢 **GitHub:** [github.com/aryadarrensetiadi](https://github.com/aryadarrensetiadi)


---
