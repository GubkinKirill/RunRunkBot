from dotenv import load_dotenv
import os
import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())