from aiogram import types

from loader import bot


async def set_default_commands():
    await bot.set_my_commands(
        [
            types.BotCommand("start", "Start bot"),
            types.BotCommand("help", "Show help"),
            types.BotCommand("inline", "Inline buttons"),
        ]
    )
