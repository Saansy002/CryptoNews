# twitter_ingest.py

import tweepy
from datetime import datetime
from config.settings import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

# --- Authenticate Twitter API ---
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET
)
api = tweepy.API(auth)

# --- Example accounts to track ---
TWITTER_ACCOUNTS = [
    "CoinDesk",
    "Cointelegraph",
    "Binance",
    "Ethereum"
]

def get_tweets(count=20):
    """
    Fetch latest tweets from predefined accounts.
    Returns a list of dicts: {text, source, link, timestamp, author}
    """
    tweets_data = []

    for username in TWITTER_ACCOUNTS:
        try:
            tweets = api.user_timeline(screen_name=username, count=count, tweet_mode="extended")
            for tweet in tweets:
                tweets_data.append({
                    "text": tweet.full_text,
                    "source": f"Twitter - {username}",
                    "link": f"https://twitter.com/{username}/status/{tweet.id}",
                    "timestamp": tweet.created_at.isoformat(),
                    "author": username
                })
        except Exception as e:
            print(f"Error fetching tweets from {username}: {e}")

    return tweets_data
