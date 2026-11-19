"""
ApnaEx Bot configuration
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Telegram credentials
API_ID = int(os.getenv("API_ID", "31585648"))
API_HASH = os.getenv("API_HASH", "269cc74123189f7bfcd9a6848380cd63")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8994641116:AAE3oJJgPKBWxbYIdMw8Sx7E_n5sFm21x_Q")
BOT_USERNAME = os.getenv("BOT_USERNAME", "@Transferoriginalfile_bot")

# Bot details
BOT_TEXT = os.getenv("BOT_TEXT", "APNAEX FILE TRANSFER BOT")
OWNER_ID = int(os.getenv("OWNER_ID", "8761631426"))

# Private Telegram channel
STORAGE_CHANNEL_ID = int(os.getenv("STORAGE_CHANNEL_ID", "-1003872490386"))
CHANNEL_ID = STORAGE_CHANNEL_ID
CHANNEL_ID2 = int(os.getenv("CHANNEL_ID2", "0"))

# MongoDB (YAHAN APNA ASLI PASSWORD DAALEIN)
MONGO_URL = os.getenv("MONGO_URL", "")
DATABASE_NAME = os.getenv("DATABASE_NAME", "apnaex")

SUDO_USERS = [
    int(user_id)
    for user_id in os.getenv("SUDO_USERS", "").split()
    if user_id.isdigit()
]

START_MESSAGE = os.getenv(
    "START_MESSAGE",
    "Welcome to ApnaEx! Send me a file to store and get a retrieval code."
)
HELP_MESSAGE = os.getenv(
    "HELP_MESSAGE",
    "Send a file to save it. Use /get CODE to retrieve a saved file."
)

def validate_config():
    missing = []

    if API_ID <= 0:
        missing.append("API_ID")
    if not API_HASH:
        missing.append("API_HASH")
    if not BOT_TOKEN:
        missing.append("BOT_TOKEN")
    if OWNER_ID <= 0:
        missing.append("OWNER_ID")
    if STORAGE_CHANNEL_ID >= 0:
        missing.append("STORAGE_CHANNEL_ID (must be a negative channel ID)")
    if not MONGO_URL:
        missing.append("MONGO_URL")

    if missing:
        raise RuntimeError(
            "Missing/invalid configuration: " + ", ".join(missing)
        )

if __name__ == "__main__":
    print("ApnaEx config.py loaded.")
