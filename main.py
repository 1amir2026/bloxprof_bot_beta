import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers.start import router as start_router
from handlers.referral import router as referral_router
from handlers.profile import router as profile_router

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(referral_router)
dp.include_router(profile_router)


async def main():
    print("✅ Bot Started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())