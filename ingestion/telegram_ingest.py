from telethon import TelegramClient
from config import settings
import asyncio

# Create client with persistent session
client = TelegramClient(
    'sessions/telegram_session',  # Session file path
    settings.TELEGRAM_API_ID,
    settings.TELEGRAM_API_HASH
)

async def fetch_messages(channel_id=settings.TELEGRAM_CHAT_ID, limit=50):
    await client.start(phone=settings.TELEGRAM_PHONE)  # Only needed for first login
    all_messages = []

    async for message in client.iter_messages(channel_id, limit=limit):
        all_messages.append(message.text)

    await client.disconnect()
    return all_messages

# For testing
if __name__ == "__main__":
    messages = asyncio.run(fetch_messages())
    print(f"Fetched {len(messages)} messages")
