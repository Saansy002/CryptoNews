# main.py

from ingestion import rss_ingest, twitter_ingest, reddit_ingest, telegram_ingest
from processing import filter_keywords, deduplicate
from storage.database import Database
from notifications import telegram_notify
import time

# --- Keywords to track ---
KEYWORDS = ["bitcoin", "ethereum", "crypto", "BNB", "ETH", "ADA"]

# --- Initialize Database ---
db = Database()
db.connect()
db.create_tables()

def run_pipeline():
    print("Starting crypto news pipeline...")

    # --- 1. Ingest Data ---
    rss_articles = rss_ingest.get_articles()
    twitter_articles = twitter_ingest.get_tweets()
    reddit_posts = reddit_ingest.get_posts()
    telegram_msgs = telegram_ingest.fetch_messages()

    all_items = rss_articles + twitter_articles + reddit_posts + telegram_msgs
    print(f"Fetched {len(all_items)} items in total.")

    # --- 2. Filter by keywords ---
    filtered_items = filter_keywords.filter_items(all_items, KEYWORDS)
    print(f"{len(filtered_items)} items after keyword filtering.")

    # --- 3. Deduplicate ---
    unique_items = deduplicate.remove_duplicates(filtered_items, db)
    print(f"{len(unique_items)} new unique items.")

    # --- 4. Store in DB & Notify ---
    for item in unique_items:
        db.insert_item(item)
        telegram_notify.send_message(item)

if __name__ == "__main__":
    while True:
        run_pipeline()
        print("Sleeping for 10 minutes before next run...")
        time.sleep(600)  # run every 10 minutes
