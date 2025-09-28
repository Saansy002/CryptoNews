import feedparser
from config.settings import NEWS_SOURCES

def fetch_news():
    """
    Fetches news from RSS feeds.
    Returns a list of dicts: text, source, link, timestamp
    """
    news_list = []
    for url in NEWS_SOURCES:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            news_list.append({
                "text": entry.get("title", ""),
                "source": url,
                "link": entry.get("link", ""),
                "timestamp": entry.get("published", "")
            })
    return news_list
