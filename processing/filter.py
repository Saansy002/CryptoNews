from config.settings import KEYWORDS

def filter_news(news_list):
    """
    Filters news based on keywords.
    Returns a list of filtered news items.
    """
    filtered = []
    for item in news_list:
        text = item.get("text", "").lower()
        if any(keyword.lower() in text for keyword in KEYWORDS):
            filtered.append(item)
    return filtered
