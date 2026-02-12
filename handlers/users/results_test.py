# from loader import dp,bot
# from aiogram import types,F,html
# from aiogram.filters import Command
# from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardButton
# from filters import IsChatAdmin
# from api import create_mypage
# # from aiogram.filters.callback_data import CallbackData
# # class GetTypeCallback(CallbackData,prefix='12456987989'):
# #     type:str
# # @dp.message(Command('results'),IsChatAdmin())
# # async def get_results(message:types.Message):
# #     btn = InlineKeyboardBuilder()
# #     btn.button(
# #         text="👥 Hamma natija",callback_data=GetTypeCallback(type='full').pack()
# #     )
# #     btn.button(text="🕔 20:30 - 20:55",callback_data=GetTypeCallback(type='part').pack())
# #     btn.adjust(1)
# #     await message.answer(f"<b>Qanday holatda javobni qabul qilasiz!</b>",reply_markup=btn.as_markup())
# # @dp.callback_query(GetTypeCallback.filter())
# # async def get_url(call:types.CallbackQuery,callback_data:GetTypeCallback):
# #     type = callback_data.type
# #     text  =  await create_mypage(type)
# #     await call.answer(cache_time=60)
# #     await call.message.answer(
# #         text =text
# #     )
# #     await call.message.delete()
