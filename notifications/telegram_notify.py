import requests
from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_message(item):
    """
    Sends a formatted Telegram message with error logging.
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": f"🚨 {item['source']} Update:\n\n{item['text']}\n\n🔗 {item['link']}",
        "disable_web_page_preview": True
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"✅ Telegram message sent: {item['source']}")
        else:
            print(f"❌ Telegram error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"⚠️ Error sending Telegram message: {e}")
