# rss_ingest.py

import feedparser
from datetime import datetime

# Example RSS feeds (crypto news, coin announcements)
RSS_FEEDS = [
    "https://cryptonews.com/news/feed",
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "https://cointelegraph.com/rss"
]

def get_articles():
    """
    Fetches articles from RSS feeds.
    Returns a list of dicts: {text, source, link, timestamp, author}
    """
    articles = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        source = feed.feed.get("title", "RSS Feed")

        for entry in feed.entries:
            article = {
                "text": entry.get("title", "") + " " + entry.get("summary", ""),
                "source": source,
                "link": entry.get("link", ""),
                "timestamp": entry.get("published", datetime.now().isoformat()),
                "author": entry.get("author", "Unknown")
            }
            articles.append(article)

    return articles
