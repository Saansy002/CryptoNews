# filter.py

import re
from utils.text_cleaner import clean_text  # optional helper to remove emojis, special chars


# ✅ Define your keywords
KEYWORDS = [
    "airdrop",
    "mainnet",
    "upgrade",
    "partnership",
    "listing",
    "fork",
    "launch",
    "hack",
    "announcement"
]

def filter_keywords(data_list):
    """
    Filters a list of data items (dicts) based on keywords.

    Each item in data_list should have a 'text' field.
    Returns only items containing at least one keyword.
    """
    filtered = []

    for item in data_list:
        text = item.get("text", "")
        text = clean_text(text)  # optional cleaning step
        text_lower = text.lower()

        if any(re.search(rf"\b{kw.lower()}\b", text_lower) for kw in KEYWORDS):
            filtered.append(item)

    return filtered
