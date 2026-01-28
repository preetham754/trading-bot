import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger():
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(f"{LOG_DIR}/bot.log")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
