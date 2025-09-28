from telegram import Bot
from config.settings import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

bot = Bot(token=TELEGRAM_TOKEN)

def send_message(item):
    """
    Sends a single news item to Telegram.
    Expects item dict with keys: text, source, link, timestamp
    """
    text = item.get("text", "")
    source = item.get("source", "")
    link = item.get("link", "")
    timestamp = item.get("timestamp", "")

    message = f"📰 *Crypto Update*\n\n"
    message += f"*Source:* {source}\n"
    message += f"*Time:* {timestamp}\n"
    message += f"*Text:* {text}\n"
    if link:
        message += f"[Link]({link})"

    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode="Markdown")
        print(f"Sent: {text[:50]}...")  # log first 50 chars
    except Exception as e:
        print(f"Error sending message: {e}")
