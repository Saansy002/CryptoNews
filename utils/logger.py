import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Generate log file name with timestamp
log_file = os.path.join(LOG_DIR, f"crypto_news_{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# Helper function for easy logging
def get_logger(name=None):
    return logging.getLogger(name)
