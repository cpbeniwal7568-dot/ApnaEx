import logging
from datetime import datetime, timezone

from pyrogram import Client, filters
from pyrogram.types import Message
from motor.motor_asyncio import AsyncIOMotorClient

from config import (
    API_ID, API_HASH, BOT_TOKEN, OWNER_ID,
    STORAGE_CHANNEL_ID, MONGO_URL, DATABASE_NAME
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
log = logging.getLogger("apnaex")

bot = Client(
    "apnaex_free_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo[DATABASE_NAME]
users = db["users"]
stored_files = db["files"]


def is_owner(user_id: int) -> bool:
    return user_id == OWNER_ID


@bot.on_message(filters.command("start") & filters.private)
async def start_handler(_, message: Message):
    user = message.from_user
    if user:
        await users.update_one(
            {"_id": user.id},
            {"$set": {
                "first_name": user.first_name or "",
                "username": user.username or "",
                "last_seen": datetime.now(timezone.utc),
            }},
            upsert=True,
        )
    await message.reply_text(
        "👋 Welcome to ApnaEx Free Bot!\n\n"
        "Send me a file, document, photo, video, or audio. "
        "I will save it to the configured private storage channel "
        "and give you a retrieval code.\n\n"
        "Use /get CODE to receive a saved file.\n"
        "Use /help for instructions."
    )


@bot.on_message(filters.command("help") & filters.private)
async def help_handler(_, message: Message):
    await message.reply_text(
        "**How to use**\n"
        "1. Send a file/media item to this bot.\n"
        "2. The bot copies it to the private storage channel.\n"
        "3. You receive a code.\n"
        "4. Send `/get CODE` to receive that file again.\n\n"
        "Only upload or share files you own or are authorized to distribute."
    )


@bot.on_message(filters.command("get") & filters.private)
async def get_handler(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Usage: /get CODE")
    code = message.command[1].strip().upper()
    record = await stored_files.find_one({"code": code})
    if not record:
        return await message.reply_text("❌ Code not found.")
    try:
        await bot.copy_message(
            chat_id=message.chat.id,
            from_chat_id=STORAGE_CHANNEL_ID,
            message_id=record["message_id"],
        )
    except Exception:
        log.exception("Could not copy stored message")
        await message.reply_text(
            "Sorry, I could not retrieve that file. Please contact the owner."
        )


@bot.on_message(
    filters.private
    & (filters.document | filters.photo | filters.video | filters.audio
       | filters.animation | filters.voice | filters.video_note)
)
async def save_media_handler(_, message: Message):
    status = await message.reply_text("⏳ Saving your file...")
    try:
        copied = await bot.copy_message(
            chat_id=STORAGE_CHANNEL_ID,
            from_chat_id=message.chat.id,
            message_id=message.id,
        )
        # Use Telegram's unique message id plus sender id as a compact retrieval code.
        code = f"{message.from_user.id % 100000:05d}{copied.id:06d}"
        await stored_files.insert_one({
            "code": code,
            "owner_id": message.from_user.id if message.from_user else None,
            "storage_chat_id": STORAGE_CHANNEL_ID,
            "message_id": copied.id,
            "created_at": datetime.now(timezone.utc),
        })
        await status.edit_text(
            f"✅ File saved successfully!\n\n"
            f"Your retrieval code: `{code}`\n"
            f"Use `/get {code}` whenever you want it back."
        )
    except Exception:
        log.exception("Saving media failed")
        await status.edit_text(
            "❌ I could not save this item. Check that the bot is an admin "
            "in the storage channel and has permission to post messages."
        )


@bot.on_message(filters.command("stats") & filters.private)
async def stats_handler(_, message: Message):
    if not message.from_user or not is_owner(message.from_user.id):
        return await message.reply_text("⛔ Owner only.")
    user_count = await users.count_documents({})
    file_count = await stored_files.count_documents({})
    await message.reply_text(
        f"**ApnaEx Stats**\nUsers: `{user_count}`\nStored files: `{file_count}`"
    )


@bot.on_message(filters.command("id") & filters.private)
async def id_handler(_, message: Message):
    await message.reply_text(f"Your Telegram ID: `{message.from_user.id}`")


if __name__ == "__main__":
    log.info("Starting ApnaEx Free Bot...")
    bot.run()
