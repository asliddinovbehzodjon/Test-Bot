from loader import dp,bot
from  aiogram import types,F
from filters import *
from aiogram.filters import Command
from keyboards.default.buttons import *
from api import *
import os
@dp.message(Command('admin'),IsChatAdmin(),IsPrivate())
async def start_admin_panel(message:types.Message):
    await message.answer("🔝 Admin panel!",reply_markup=admin_button())
# @dp.message(F.text=='🗣 Reklama yuborish',IsChatAdmin(),IsPrivate())
# async def get_add_type(message:types.Message):
#     await message.answer("Qaysi turdagi xabar yuborasiz!\n"
#                          "Tanlang👇",reply_markup=add_type())
# Back Button
@dp.message(F.text=='⏺ Bekor qilish',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=add_type())
@dp.message(F.text=='🆗 Kerakmas',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=add_type())
@dp.message(F.text=='📊 Obunachilar soni',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    count = await users_count()
    await message.answer(f"Bot hozir {count} ta faol obunachi bor!")


@dp.message(Command('clear'),IsChatAdmin(),IsPrivate())
async def clear(message:types.Message):
    try:
        import os
        for filename in os.listdir():
            if filename.endswith(('.mp4', '.avi', '.mkv', '.mov','.mp3','.webm','.webm.part')):
                    os.remove(filename)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    await message.answer('Kesh tozalandi!',reply_markup=types.ReplyKeyboardRemove())
@dp.message(Command('folder'),IsChatAdmin(),IsPrivate())
async def folder(message:types.Message):
    text = str(os.listdir())
    await message.answer(text,reply_markup=types.ReplyKeyboardRemove())

from states.mystate import NewPost
def test_button_back():
    button = ReplyKeyboardBuilder()
   
    button.row(
        
        KeyboardButton(text="⬅️ Orqaga")
        
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
from aiogram.fsm.context import FSMContext
from aiogram import html
@dp.message(F.text=="🗣 Reklama yuborish",IsChatAdmin())
async def start(message:types.Message,state:FSMContext):
    await message.answer(html.bold('Reklama matnini yuboring!'),reply_markup=test_button_back())
    await state.set_state(NewPost.NewMessage)
@dp.message(NewPost.NewMessage,IsPrivate(),IsChatAdmin())
async def start(message:types.Message,state:FSMContext):
    if message.text=="⬅️ Orqaga":
         await message.answer('🔝 Asosiy sahifa',reply_markup=admin_button())
         await state.clear()
    else:
        counter = 0
        users = await get_all_users()
        print(users)
        
            
        for user in users:
                
                try:
                    await bot.copy_message(
                chat_id=user['telegram_id'],
                from_chat_id=message.chat.id,
                message_id=message.message_id,
                
            )
                    await asyncio.sleep(1)
                    counter+=1
                except Exception as e:
                    print(e)
       
        await message.answer(html.bold(f"{counter} ta foydalanuvchiga xabar yuborildi!"))
        await state.clear()
