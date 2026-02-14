from loader import dp,bot
from aiogram import types,html,F
# from api import results_of_test
from telegraph.aio import Telegraph
from aiogram.filters import Command
from keyboards.default.buttons import *

@dp.message(F.text=="🤖 Bot haqida ma’lumot")
async def test(message:types.Message):
    text = f"@Aqilli_testbot haqida to'liq ma'lumotni @Aqilli_testbot_haqida kanalidan o'qib olishingiz mumkin.\n"\
f"(Kanalga a'zo bo'lish majburiy emas, shunchaki kirib botning imkoniyatlari bilan tanishib chiqishingiz mumkin)"
    await message.answer(html.bold(text))
@dp.message(F.text=="⬅️ Orqaga")
async def test(message:types.Message):
    await message.answer(
         "🔝 Asosiy Menyu",reply_markup=main_button()
      )


