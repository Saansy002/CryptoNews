import time
from ingestion.fetch_news import fetch_news
from processing.filter import filter_news
from notifications.telegram_notify import send_message

# Interval in seconds (e.g., 15 minutes = 900 seconds)
INTERVAL = 900  # 15 minutes

def run():
    while True:
        print("Fetching crypto news...")
        
        # 1. Fetch all news
        news_list = fetch_news()

        # 2. Filter news based on keywords
        filtered_news = filter_news(news_list)

        # 3. Send filtered news to Telegram
        if filtered_news:
            for item in filtered_news:
                send_message(item)
        else:
            print("No news matched keywords this cycle.")

        print(f"Sleeping for {INTERVAL // 60} minutes...\n")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    run()
