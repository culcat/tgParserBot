import csv
import os
from telethon import TelegramClient
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

client = TelegramClient('session_name', api_id, api_hash)

async def async_parse_channel_to_csv(channel_username: str) -> Path:
    await client.start()
    try:
        messages = await client.get_messages(channel_username, limit=100)

        filename = f"{channel_username.strip('@')}.csv"
        csv_path = Path.cwd() / filename

        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["text"])
            writer.writeheader()
            for message in messages:
                writer.writerow({'text': message.text or ''})

        return csv_path

    finally:
        await client.disconnect()