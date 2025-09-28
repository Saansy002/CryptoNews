# deduplicate.py

import hashlib

def generate_hash(item):
    """
    Generates a unique hash for each item based on text + source + timestamp.
    """
    text = item.get("text", "")
    source = item.get("source", "")
    timestamp = item.get("timestamp", "")
    combined = f"{text}-{source}-{timestamp}"
    return hashlib.md5(combined.encode("utf-8")).hexdigest()


def remove_duplicates(data_list, db):
    """
    Removes items already in the database.
    Assumes db has a method `exists(hash)` to check if item exists.
    """
    unique_items = []

    for item in data_list:
        item_hash = generate_hash(item)
        if not db.exists(item_hash):
            item["hash"] = item_hash  # store hash for later insertion
            unique_items.append(item)

    return unique_it_
