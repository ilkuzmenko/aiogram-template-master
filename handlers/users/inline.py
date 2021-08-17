from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from loader import dp


@dp.message_handler(Command("inline"))
async def random_command(message: Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="⬅️", callback_data="prev_page"),
                 types.InlineKeyboardButton(text="➡️", callback_data="next_page"))
    await message.answer("Press the button to use inline buttons", reply_markup=keyboard)


@dp.callback_query_handler(text="prev_page")
async def prev_page(call: types.CallbackQuery):
    await call.message.answer("⬅️")
    await call.answer()


@dp.callback_query_handler(text="next_page")
async def next_page(call: types.CallbackQuery):
    await call.message.answer("➡️")
    await call.answer(text="Pop-up window", show_alert=True)
