"""
ApnaEx Bot configuration
Style: simple centralized settings, inspired by the public ApnaEx config layout.
Keep secrets in hosting Environment Variables or a private .env file.
NEVER commit your real BOT_TOKEN, API_HASH, or MONGO_URL to public GitHub.
"""

import os
from dotenv import load_dotenv

# Load local .env when running on your own computer.
# On hosting, add these values in the Environment Variables section.
load_dotenv()

# Telegram credentials
API_ID = int(os.getenv("API_ID", "31585648"))
API_HASH = os.getenv("API_HASH", "269cc74123189f7bfcd9a6848380cd63")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8994641116:AAE3oJJgPKBWxbYIdMw8Sx7E_n5sFm21x_Q")
BOT_USERNAME = os.getenv("BOT_USERNAME", "@Transferoriginalfile_bot")

# Bot details
BOT_TEXT = os.getenv("BOT_TEXT", "APNAEX FILE TRANSFER BOT")
OWNER_ID = int(os.getenv("OWNER_ID", "8761631426"))

# Private Telegram channel where uploaded files are stored.
# Use the channel ID beginning with -100.
STORAGE_CHANNEL_ID = int(os.getenv("STORAGE_CHANNEL_ID", "-1003872490386"))

# Compatibility aliases for projects/config layouts using CHANNEL_ID.
CHANNEL_ID = STORAGE_CHANNEL_ID
CHANNEL_ID2 = int(os.getenv("CHANNEL_ID2", "0"))

# MongoDB
MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://cpbeniwal7568_db_user:<db_password>@cluster0.c2fwzua.mongodb.net/"
)
DATABASE_NAME = os.getenv("DATABASE_NAME", "apnaex")

# Optional admin IDs separated by spaces, e.g. "123456 987654"
SUDO_USERS = [
    int(user_id)
    for user_id in os.getenv("SUDO_USERS", "").split()
    if user_id.isdigit()
]

# Optional text settings
START_MESSAGE = os.getenv(
    "START_MESSAGE",
    "Welcome to ApnaEx! Send me a file to store and get a retrieval code."
)
HELP_MESSAGE = os.getenv(
    "HELP_MESSAGE",
    "Send a file to save it. Use /get CODE to retrieve a saved file."
)


def validate_config():
    """Check required settings before the bot starts."""
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
        missing.append("STORAGE_CHANNEL_ID (must be a negative channel ID, usually starts with -100)")
    if not MONGO_URL:
        missing.append("MONGO_URL")

    if missing:
        raise RuntimeError(
            "Missing/invalid configuration: " + ", ".join(missing)
            + ". Add these values in your hosting Environment Variables."
        )


if __name__ == "__main__":
    print("ApnaEx config.py loaded.")
    print("API_ID set:", API_ID > 0)
    print("API_HASH set:", bool(API_HASH))
    print("BOT_TOKEN set:", bool(BOT_TOKEN))
    print("OWNER_ID set:", OWNER_ID > 0)
    print("STORAGE_CHANNEL_ID set:", STORAGE_CHANNEL_ID < 0)
    print("MONGO_URL set:", bool(MONGO_URL))
