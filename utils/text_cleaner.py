# text_cleaner.py

import re

def clean_text(text):
    """
    Cleans text by removing URLs, emojis, extra spaces, and special chars.
    """
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)
    # Remove emojis
    text = re.sub(r"[^\w\s.,!?'-]", "", text)
    # Normalize spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text
