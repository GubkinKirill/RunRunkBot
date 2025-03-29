from dotenv import load_dotenv
import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart


load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer('Hello')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())