import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

from bot.handlers.user_handlers import reg_handler


async def main() -> None:
    
    load_dotenv(".env")

    storage = MemoryStorage()

    token = os.getenv("TOKEN")
    bot = Bot(token)
    dp = Dispatcher(bot, storage=storage)
    
    reg_handler(dp)

    try:
        await dp.start_polling(bot)
    except:
        await bot.session.close()
        await bot.close()
        print("Bot is stop!")


if __name__ == "__main__":
    asyncio.run(main())
