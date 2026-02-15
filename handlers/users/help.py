from aiogram import types,html
from aiogram.filters import Command
from loader import dp
from write_sertificate import *
from aiogram.types import BufferedInputFile
from aiogram import types
from loader import dp
from aiogram import html
from handlers.users.start import text


@dp.message(Command('help'))
async def bot_help(message: types.Message):
    await message.answer(text(message.from_user.full_name))

