import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sqlite3

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Fetch crypto news using NewsAPI
def fetch_news(api_key, query="cryptocurrency", max_results=10):
    url = f"https://newsapi.org/v2/everything?q={query}&pageSize={max_results}&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get("articles", [])

# Analyze sentiment of news articles
def analyze_sentiment(articles):
    sentiment_data = []
    for article in articles:
        text = f"{article['title']} {article.get('description', '')} {article.get('content', '')}"
        score = analyzer.polarity_scores(text)
        sentiment_data.append({
            "title": article["title"],
            "sentiment": score["compound"],
            "positive": score["pos"],
            "neutral": score["neu"],
            "negative": score["neg"]
        })
    return sentiment_data

# Store sentiment data into SQLite
def store_sentiment_data(data, db_name="crypto_sentiment.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news_sentiment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            sentiment REAL,
            positive REAL,
            neutral REAL,
            negative REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    for item in data:
        cursor.execute('''
            INSERT INTO news_sentiment (title, sentiment, positive, neutral, negative)
            VALUES (?, ?, ?, ?, ?)
        ''', (item["title"], item["sentiment"], item["positive"], item["neutral"], item["negative"]))
    conn.commit()
    conn.close()

# Main execution
if __name__ == "__main__":
    api_key = "55c1ab2a22bd4c588300e0646729af33"  # Replace with your NewsAPI key
    articles = fetch_news(api_key)
    sentiment_data = analyze_sentiment(articles)
    store_sentiment_data(sentiment_data)
