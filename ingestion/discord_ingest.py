import requests
import json
from config.settings import DISCORD_BOT_TOKEN, DISCORD_CHANNEL_ID

BASE_URL = "https://discord.com/api/v10"

def fetch_discord_messages(limit=10):
    url = f"{BASE_URL}/channels/{DISCORD_CHANNEL_ID}/messages?limit={limit}"
    headers = {
        "Authorization": f"Bot {DISCORD_BOT_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch messages: {response.status_code}")
        return []

    messages = response.json()
    # Only get text content
    return [msg["content"] for msg in messages if "content" in msg]

# Example usage
if __name__ == "__main__":
    messages = fetch_discord_messages()
    for m in messages:
        print(m)
