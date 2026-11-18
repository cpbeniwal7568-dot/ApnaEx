"""Configuration loaded from environment variables."""
import os
from dotenv import load_dotenv

load_dotenv()

def required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

API_ID = int(required("API_ID"))
API_HASH = required("API_HASH")
BOT_TOKEN = required("BOT_TOKEN")
OWNER_ID = int(required("OWNER_ID"))
STORAGE_CHANNEL_ID = int(required("STORAGE_CHANNEL_ID"))
MONGO_URL = required("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME", "ApnaEx")
