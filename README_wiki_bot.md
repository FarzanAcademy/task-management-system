This repository adds a simple Telegram bot that looks up person names on Wikipedia and returns a thumbnail image if available.

Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set your Telegram bot token in the environment (PowerShell example):

```powershell
$env:TELEGRAM_BOT_TOKEN = "<your-token-here>"
python shervin_robot.py
```

Usage

- Send `/start` to the bot for instructions.
- Send a person's name (e.g. "Albert Einstein") and the bot will attempt to return a Wikipedia thumbnail for that person.

Notes

- This simple implementation uses the English Wikipedia and works best for notable people who have pages with images.
- If you need broader image sources (Google/Bing), you'll need API keys and a different implementation.
