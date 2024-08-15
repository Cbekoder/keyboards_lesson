from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import html
from bot.keyboards.inline.mainKeyboard import mainButtons

from loader import dp

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!", reply_markup=mainButtons)
