"""
ApnaEx Free Bot - configuration template

Keep all secrets in your hosting provider's Environment Variables.
Do NOT commit real tokens, API hashes, passwords, or MongoDB URLs to GitHub.
"""

import os

# Telegram API credentials (set these as environment variables)
API_ID = int(os.getenv("31585648", "0"))
API_HASH = os.getenv("269cc74123189f7bfcd9a6848380cd63", "")
BOT_TOKEN = os.getenv("8994641116:AAE3oJJgPKBWxbYIdMw8Sx7E_n5sFm21x_Q", "")

# Bot identity
BOT_USERNAME = "Transferoriginalfile_bot"

# Owner and channel
OWNER_ID = 8761631426
CHANNEL_ID = -1003872490386

# MongoDB connection (set the COMPLETE URI as MONGO_URL in hosting)
MONGO_URL = os.getenv("mongodb+srv://cpbeniwal7568_db_user:YOUR_NEW_PASSWORD@cluster0.c2fwzua.mongodb.net/ApnaEx?compressors=zlib", "")

# Optional features
# This project is intended to run without Premium or thumbnail features.
# Remove any corresponding imports/references in the bot's other files too.
