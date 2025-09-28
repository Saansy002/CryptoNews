def exists(self, item_hash):
    query = "SELECT 1 FROM news WHERE hash = ? LIMIT 1"
    self.cursor.execute(query, (item_hash,))
    return self.cursor.fetchone() is not None
# database.py

import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="crypto_news.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    # Connect to SQLite
    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    # Create table if it doesn't exist
    def create_tables(self):
        query = """
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hash TEXT UNIQUE,
            source TEXT,
            author TEXT,
            timestamp TEXT,
            text TEXT,
            link TEXT
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    # Insert new item
    def insert_item(self, item):
        query = """
        INSERT INTO news (hash, source, author, timestamp, text, link)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            self.cursor.execute(query, (
                item.get("hash"),
                item.get("source"),
                item.get("author"),
                item.get("timestamp"),
                item.get("text"),
                item.get("link")
            ))
            self.conn.commit()
        except sqlite3.IntegrityError:
            # Duplicate hash, skip insertion
            pass

    # Check if item exists by hash
    def exists(self, item_hash):
        query = "SELECT 1 FROM news WHERE hash = ? LIMIT 1"
        self.cursor.execute(query, (item_hash,))
        return self.cursor.fetchone() is not None

    # Optional: fetch latest N items
    def fetch_latest(self, limit=50):
        query = "SELECT * FROM news ORDER BY timestamp DESC LIMIT ?"
        self.cursor.execute(query, (limit,))
        return self.cursor.fetchall()

    # Close connection
    def close(self):
        self.conn.close()
