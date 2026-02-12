from loader import dp,bot
from aiogram import types,suppress,html
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram import F
from keyboards.inline.buttons import *
from api import *
from checktest import *
from environs import Env
from keyboards.default.buttons import *
from middlewares.mymiddleware import *
from aiogram.fsm.context import FSMContext
from states.mystate import *
# Check Answers With Write by Hand
@dp.message(F.text.startswith('Mening ma’lumotlarim'))
async def attestat(message:types.Message,state:FSMContext):
      user_id = message.from_user.id
      user =  await get_user(telegram_id=user_id)
      print(user)
      if user['role'] =='📚 Repetitor':
          role = True
          await message.answer(
              text=f"👤 Mening ma'lumotlarim.\n\n"
                   f"✅ <b>Ism Familya: </b><b><i>{user['name']}</i></b>\n\n"
                   f"✅ <b>Faoliyatiz: </b><b><i>{user['role']}</i></b>\n\n" 
                   f"✅ <b>Kanalingiz: </b><b><i>{user['guruh']}</i></b>\n" 
              ,
              reply_markup=change_info_button(role=role)  )
      else:
           user = await get_user(telegram_id=message.from_user.id)          
           role =False
           await message.answer(
              text=f"👤 Mening ma'lumotlarim.\n\n"
                   f"✅ <b>Ism Familya: </b><b><i>{user['name']}</i></b>\n\n"
                   f"✅ <b>Faoliyatiz: </b><b><i>{user['role']}</i></b>\n" 
              ,
              reply_markup=change_info_button(role=role)  )
# Change Name 
@dp.message(F.text.startswith("🔄 Ism-familyani o'zgartirish"))
async def attestat(message:types.Message,state:FSMContext):
      user_id = message.from_user.id
      
      await message.answer(
          text= f"<b>FISH kiriting.</b>\nMasalan: <b> Asliddinov Behzod Furqat o'g'li </b>"
      )
      await state.set_state(UserChangeNameData.name)
@dp.message(F.text,UserChangeNameData.name)
async def get_name(message:types.Message,state:FSMContext):
   await state.update_data(
      {
         'name':message.text
      }
   )
   await change_user_name(telegram_id=message.from_user.id,name=message.text)
   user =  await get_user(telegram_id=message.from_user.id)
   print(user)
   if user['role'] =='📚 Repetitor':
      role = True
      await message.answer(
              text=f"👤 Mening ma'lumotlarim.\n\n"
                   f"✅ <b>Ism Familya: </b><b><i>{user['name']}</i></b>\n\n"
                   f"✅ <b>Faoliyatiz: </b><b><i>{user['role']}</i></b>\n\n" 
                   f"✅ <b>Kanalingiz: </b><b><i>{user['guruh']}</i></b>\n" 
              ,
              reply_markup=change_info_button(role=role)  )
   else:
        user = await get_user(telegram_id=message.from_user.id)          
        role =False
        await message.answer(
          text=f"👤 Mening ma'lumotlarim.\n\n"
                f"✅ <b>Ism Familya: </b><b><i>{user['name']}</i></b>\n\n"
                f"✅ <b>Faoliyatiz: </b><b><i>{user['role']}</i></b>\n" 
          ,
          reply_markup=change_info_button(role=role)  )
   await state.clear()
# Change Role 
@dp.message(F.text.startswith("ℹ️ Faoliyat turini o'zgartirish"))
async def attestat(message:types.Message,state:FSMContext):
    await message.answer(
      f"<b>Siz kim bo‘lib faoliyat yuritasiz?</b>\nMasalan: <b>O'qituvchi</b>",reply_markup=choose_role()
      
   )
    await state.set_state(UserChangeRoleData.role)
@dp.message(F.text,UserChangeRoleData.role)
async def get_name(message:types.Message,state:FSMContext):
    if message.text in ["🧑‍🏫 O'qituvchi","🧑‍🎓 O'quvchi",'📚 Repetitor']:
      await change_user_role(telegram_id=message.from_user.id,role=message.text)
      user =  await get_user(telegram_id=message.from_user.id)
      print(user)
      if user['role'] =='📚 Repetitor':
          role = True
          await message.answer(
              text=f"👤 Mening ma'lumotlarim.\n\n"
                   f"✅ <b>Ism Familya: </b><b><i>{user['name']}</i></b>\n\n"
                   f"✅ <b>Faoliyatiz: </b><b><i>{user['role']}</i></b>\n\n" 
                   f"✅ <b>Kanalingiz: </b><b><i>{user['guruh']}</i></b>\n" 
              ,
              reply_markup=change_info_button(role=role)  )
      else:
           user = await get_user(telegram_id=message.from_user.id)          
           role =False
           await message.answer(
              text=f"👤 Mening ma'lumotlarim.\n\n"
                   f"✅ <b>Ism Familya: </b><b><i>{user['name']}</i></b>\n\n"
                   f"✅ <b>Faoliyatiz: </b><b><i>{user['role']}</i></b>\n" 
              ,
              reply_markup=change_info_button(role=role)  )
      await state.clear()
    
    else:
      await message.answer(
      f"<b>Siz kim bo‘lib faoliyat yuritasiz?</b>\nMasalan: <b>O'qituvchi</b>",reply_markup=choose_role()
      
   )
      await state.set_state(UserChangeRoleData.role)
# Change Channel 
@dp.message(F.text.startswith("🔗 Kanalni o'zgartirish"))
async def attestat(message:types.Message,state:FSMContext):
    await message.answer(
      f"<b> Sertifikatda ko‘rinishi uchun kanalingiz nomini yozing (@ bilan)</b>\nMasalan: <b>@Bekhzod_Asliddinov</b>")
  
    await state.set_state(UserChangeGroupData.group)
   
@dp.message(F.text,UserChangeGroupData.group)
async def get_name(message:types.Message,state:FSMContext):
      await change_user_group(telegram_id=message.from_user.id,guruh=message.text)
      user =  await get_user(telegram_id=message.from_user.id)
      print(user)
      if user['role'] =='📚 Repetitor':
          role = True
          await message.answer(
              text=f"👤 Mening ma'lumotlarim.\n\n"
                   f"✅ <b>Ism Familya: </b><b><i>{user['name']}</i></b>\n\n"
                   f"✅ <b>Faoliyatiz: </b><b><i>{user['role']}</i></b>\n\n" 
                   f"✅ <b>Kanalingiz: </b><b><i>{user['guruh']}</i></b>\n" 
              ,
              reply_markup=change_info_button(role=role)  )
      else:
           user = await get_user(telegram_id=message.from_user.id)          
           role =False
           await message.answer(
              text=f"👤 Mening ma'lumotlarim.\n\n"
                   f"✅ <b>Ism Familya: </b><b><i>{user['name']}</i></b>\n\n"
                   f"✅ <b>Faoliyatiz: </b><b><i>{user['role']}</i></b>\n" 
              ,
              reply_markup=change_info_button(role=role)  )
      await state.clear()
