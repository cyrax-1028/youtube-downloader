from aiogram import types
from config import ADMIN_ID
from database import get_all_users

async def send_ad_message(dp, message: types.Message):
    if message.from_user.id == ADMIN_ID:
        text = message.text.replace("/send ", "")
        users = get_all_users()
        for user in users:
            try:
                await dp.bot.send_message(user, text)
            except:
                pass
