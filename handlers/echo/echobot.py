from aiogram import types
from loader import dp
from aiogram import html
from handlers.users.start import text
@dp.message()
async def default(message: types.Message):
  
    await message.answer(text(message.from_user.full_name))

