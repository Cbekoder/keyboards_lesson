from asyncio import timeout

from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.states.registerData import RegisterForm

from loader import dp


@dp.callback_query(lambda callback: callback.data == 'register')
async def registerStartHandler(callback: CallbackQuery, state: FSMContext):
    await callback.answer(cache_time=10)
    await state.set_state(RegisterForm.name)

    await callback.message.answer(
        "Hi there! What's your name?",
    )


@dp.message(RegisterForm.name)
async def registerNameHandler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RegisterForm.email)
    await message.answer("Enter your email:")


@dp.message(RegisterForm.email)
async def registerEmailHandler(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await state.set_state(RegisterForm.phone)
    await message.answer("Enter your Phone number:")

@dp.message(RegisterForm.phone)
async def registerEmailHandler(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(RegisterForm.address)
    await message.answer("Enter your address:")

@dp.message(RegisterForm.address)
async def registerEmailHandler(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    data = await state.get_data()
    response = f"I get into about you\nName: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nAddress: {data['address']}"
    await message.answer(response)
