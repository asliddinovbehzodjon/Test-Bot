import logging
from aiogram import types,html,F
from aiogram.filters import Command
from loader import bot, dp
from api import *
from states.mystate import UserGetData
from aiogram.fsm.context import FSMContext
from keyboards.default.buttons import *
# Start Command
def text(fullname):
    return (f"<b>👋 Assalomu alaykum {fullname}!</b>\n\n"
            f"<i>🤖 Men sizga test tekshirishga yordam beraman!</i>\n"
           
            )
@dp.message(F.text=="❌ Bekor qilish")
async def show_channels(message: types.Message,state:FSMContext):
  
      await message.answer(
        "🔝 Asosiy Menyu",reply_markup=main_button()
      )
      await state.clear()
@dp.message(Command('start'))
async def show_channels(message: types.Message,state:FSMContext):
   user = await get_user(message.from_user.id)
   if user=={}:
      await message.answer(
         f"👋 Assalomu alaykum <b>{message.from_user.full_name}</b>!\n\n"
         f"<i>✅ Test ishlashdan oldin ro'yxadan o'tish kerak!</i>\n\n"
         f"<b>FISH kiriting.</b>\nMasalan: <b> Axmedov Fazliddin </b>"
      )
      await state.set_state(UserGetData.name)
   else:
      await message.answer(
        "🔝 Asosiy Menyu",reply_markup=main_button()
      )
@dp.message(F.text,UserGetData.name)
async def get_name(message:types.Message,state:FSMContext):
   await state.update_data(
      {
         'name':message.text
      }
   )
   await message.answer(
      f"<b>Siz kim bo‘lib faoliyat yuritasiz?</b>\nMasalan: <b>O'qituvchi</b>",reply_markup=choose_role()
      
   )
   await state.set_state(UserGetData.role)

@dp.message(F.text,UserGetData.role)
async def get_role(message:types.Message,state:FSMContext):
   if message.text in ["🧑‍🏫 O'qituvchi","🧑‍🎓 O'quvchi",'📚 Repetitor']:
      await state.update_data(
         {
            'role':message.text
         }
      )
      if message.text == "🧑‍🏫 O'qituvchi":
         await message.answer(
      f"<b>Qaysi fan o'qituvchisisiz?</b>\nMasalan: <b>Matematika</b>")
      elif message.text == "🧑‍🎓 O'quvchi":
          await message.answer(
      f"<b>Nechanchi sinfdasiz?</b>\nMasalan: <b>6-sinf</b>")
      else:
          await message.answer(
      f"<b> Sertifikatda ko‘rinishi uchun kanalingiz nomini yozing (@ bilan)</b>\nMasalan: <b>@Korgazmali_talim</b>")
      await state.set_state(UserGetData.group)  
    
   else:
      await message.answer(
      f"<b>Siz kim bo‘lib faoliyat yuritasiz?</b>\nMasalan: <b>O'qituvchi</b>",reply_markup=choose_role()
      
   )
      await state.set_state(UserGetData.group)
@dp.message(F.text,UserGetData.group)
async def get_group(message:types.Message,state:FSMContext):
      await state.update_data(
         {
            'group':message.text
         }
      )
      data = await state.get_data()
      try:
         await create_user(
            telegram_id=message.from_user.id,
            name=data.get('name',None),
            role=data.get('role',None),
            group=data.get('group',None)
         )
      except Exception as e:
         print(e)
         pass
      await message.answer(
         "🔝 Asosiy Menyu",reply_markup=main_button()
      )
      await state.clear()
   