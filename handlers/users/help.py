from aiogram import types,html
from aiogram.filters import Command
from loader import dp
from write_sertificate import *
from aiogram.types import BufferedInputFile
@dp.message(Command('help'))
async def bot_help(message: types.Message):
    image_bytes = write_attestat_image(author='Behzod Asliddinov',student='Axmedov Fazliddin',degree=86,channel='@Korgazmali_talim')
    photo = BufferedInputFile(
        image_bytes.read(),
        filename="image.png"
    )
    await message.answer_photo(photo=photo, caption="Generated image")