import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv
from parse_tg import async_parse_channel_to_csv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
@dp.message(Command("help"))
async def send_welcome(message: Message):
    await message.answer(
        "Это бот для парсинга телеграм каналов\n"
        "Отправь имя канала и получи все сообщения в формате CSV.\n"
        "Пример: @faithinmyselff"
    )

@dp.message()
async def handle_channel(message: Message):
    await message.answer("Начинаю парсинг канала, подожди немного...")
    try:
        await async_parse_channel_to_csv(message.text)
        await message.answer("Парсинг завершен ✅. Файл будет доступен позже (или реализуй отправку файла).")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())