import requests

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

def handle_update(update):
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "Welcome to the CNC Coin Telegram Bot!")
        elif text.startswith("/referral"):
            send_message(chat_id, "Track your referrals via our mini app.")