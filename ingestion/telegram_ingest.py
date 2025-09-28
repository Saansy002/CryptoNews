# telegram_ingest.py

from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from config.settings import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_PHONE
from datetime import datetime
import asyncio

# --- Channels to track ---
CHANNELS = [
    "Crypto_PumpSignals",
    "BinanceAnnouncements",
    "EthereumAnnouncements"
]

# Initialize Telegram client
client = TelegramClient('crypto_session', TELEGRAM_API_ID, TELEGRAM_API_HASH)

async def get_channel_messages(limit=20):
    """
    Fetch latest messages from predefined Telegram channels/groups.
    Returns a list of dicts: {text, source, link, timestamp, author}
    """
    messages_data = []

    await client.start(phone=TELEGRAM_PHONE)

    for channel in CHANNELS:
        try:
            entity = await client.get_entity(channel)
            history = await client.get_messages(entity, limit=limit)
            for msg in history:
                messages_data.append({
                    "text": msg.message or "",
                    "source": f"Telegram - {channel}",
                    "link": f"https://t.me/{channel}/{msg.id}",
                    "timestamp": msg.date.isoformat(),
                    "author": msg.sender_id
                })
        except Exception as e:
            print(f"Error fetching messages from {channel}: {e}")

    await client.disconnect()
    return messages_data

def fetch_messages(limit=20):
    return asyncio.run(get_channel_messages(limit))
