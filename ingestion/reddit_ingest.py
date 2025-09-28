# reddit_ingest.py

import praw
from datetime import datetime
from config.settings import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

# --- Authenticate Reddit API ---
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

# --- Subreddits to track ---
SUBREDDITS = [
    "cryptocurrency",
    "CryptoMarkets",
    "ethtrader",
    "Bitcoin"
]

def get_posts(limit=20):
    """
    Fetch latest posts from predefined subreddits.
    Returns a list of dicts: {text, source, link, timestamp, author}
    """
    posts_data = []

    for subreddit_name in SUBREDDITS:
        subreddit = reddit.subreddit(subreddit_name)
        try:
            for submission in subreddit.new(limit=limit):
                posts_data.append({
                    "text": submission.title + " " + (submission.selftext or ""),
                    "source": f"Reddit - {subreddit_name}",
                    "link": submission.url,
                    "timestamp": datetime.fromtimestamp(submission.created_utc).isoformat(),
                    "author": submission.author.name if submission.author else "Unknown"
                })
        except Exception as e:
            print(f"Error fetching posts from {subreddit_name}: {e}")

    return posts_data
