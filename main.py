import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command  # Yangi qo‘shildi
from aiogram.types import Message
from config import TOKEN, ADMIN_ID
from downloader import download_youtube, download_instagram
from database import add_user
from admin import send_ad_message

logging.basicConfig(level=logging.INFO)

# Aiogram 3.x uchun to‘g‘ri konfiguratsiya
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Botni boshlash
@dp.message(Command("start"))  # YANGI TO‘G‘RI USUL
async def start(message: Message):
    add_user(message.from_user.id)
    await message.answer("🎥 Salom! Menga YouTube yoki Instagram havolasini yuboring.")

# Admin uchun reklama yuborish
@dp.message(Command("send"))  # To‘g‘ri usul
async def send_advertisement(message: Message):
    await send_ad_message(dp, message)

# Video yuklash
from aiogram.types import FSInputFile  # Import qilish kerak

@dp.message(F.text)  # Har qanday matnli xabarni tutib olish
async def download_video(message: Message):
    url = message.text

    if "youtube.com" in url or "youtu.be" in url:
        await message.answer("⏳ Yuklab olinmoqda...")
        file_path = download_youtube(url)

        video = FSInputFile(file_path)  # To‘g‘ri usul
        await message.answer_video(video)

        os.remove(file_path)  # Yuklangan faylni o‘chirish

    elif "instagram.com" in url:
        await message.answer("⏳ Yuklab olinmoqda...")
        video_url = download_instagram(url)
        await message.answer_video(video_url)

    else:
        await message.answer("❌ Noto‘g‘ri havola. Faqat YouTube yoki Instagram havolasini yuboring.")

# Botni ishga tushirish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
