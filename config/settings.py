from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Telegram Bot
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Twitter API
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Reddit API
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Telegram API (Telethon)
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
TELEGRAM_PHONE = os.getenv("TELEGRAM_PHONE")

# Discord Bot
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")
# Telegram Configuration
TELEGRAM_TOKEN = "8204594506:AAH9hKsnUKHqzJvXON2qPtxVIE4T_wR6d8"
TELEGRAM_CHAT_ID = "1829036467"

# Keywords for filtering
KEYWORDS = ["Bitcoin", "Ethereum", "Crypto", "DeFi", "Altcoins"]

# News sources (RSS feeds)
NEWS_SOURCES = [
    "https://cryptonews.com/news/rss/",
    "https://cointelegraph.com/rss",
    "https://coindesk.com/arc/outboundfeeds/rss/"
]
