# ApnaEx Free Telegram Bot

A simple, free Telegram file-storage and retrieval bot built with Pyrogram and MongoDB.

## Features
- Users send a document/photo/video/audio to the bot.
- Bot copies the message into your private storage channel.
- Bot returns a retrieval code.
- `/get CODE` copies the stored message back to the user.
- `/stats` is available to the configured owner.
- No premium, payment, or thumbnail features.

## Requirements
- Python 3.10.11
- A Telegram bot token from BotFather
- Telegram API ID and API hash
- A MongoDB connection string
- A private Telegram channel where the bot is an administrator with permission to post

## Setup
1. Extract this ZIP.
2. Install Python 3.10.11.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Copy `.env.example` to `.env`.
5. Fill in the values in `.env`. Do not upload `.env` to GitHub.
6. Add your bot to the private storage channel as an administrator and allow it to post messages.
7. Run:
   `python app.py`

## Commands
- `/start` - start the bot
- `/help` - usage instructions
- `/get CODE` - retrieve a saved file
- `/stats` - owner-only usage counts
- `/id` - show your Telegram user ID

## Important security notes
- Any bot token, API hash, or database password previously pasted into chats or public repositories should be rotated before use.
- Keep `.env` private. Commit only `.env.example`.
- Use this bot only for files you own or have permission to store and redistribute.
- This is a starter implementation. Telegram's platform limits, channel permissions, and hosting limits apply.
- Retrieval codes are convenient identifiers, not private access controls. Anyone who obtains a code may be able to request that file. Add ownership checks before using it for sensitive files.
