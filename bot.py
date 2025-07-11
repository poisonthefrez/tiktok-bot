import sys
import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from keep_alive import keep_alive

from handlers import commands

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

keep_alive()

async def main():
    load_dotenv()
    token = os.getenv('BOT_TOKEN')
    bot = Bot(token)
    dp = Dispatcher()

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    dp.include_router(commands.router)

    print('Bot Start')
    await dp.start_polling(bot)
    await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')
