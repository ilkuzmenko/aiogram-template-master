import asyncio

from config import ADMIN
from loader import bot
from utils.asyncpg_db.create_tables import create_user_db
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    await asyncio.sleep(5)

    await create_user_db()

    # Set default bot commands
    await set_default_commands()

    # Notify admins about start up
    await bot.send_message(ADMIN, "Bot launched")


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
