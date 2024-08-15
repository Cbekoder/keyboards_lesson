from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup

from bot.keyboards.default.keyboardMenu import menu

from loader import dp


@dp.message(Command('menu'))
async def start_menu(message: Message):
    await message.reply("Menuni tanlash", reply_markup=menu)


@dp.message(lambda message: message.text == "Kategoriyalar")
async def kategoriyalar(message: Message):
    await message.answer("Kategoriyalar Nima", reply_markup=ReplyKeyboardRemove())