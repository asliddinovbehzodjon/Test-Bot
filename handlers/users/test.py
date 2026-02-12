# from loader import dp,bot
# from aiogram import types,suppress,html
# from aiogram.exceptions import TelegramBadRequest
# from aiogram.filters import Command
# from aiogram import F
# from keyboards.inline.buttons import *
# from api import *
# from checktest import *
# from environs import Env
# numbers_icon = {
#     1:'1️⃣',
#     2:'2️⃣',
#     3:'3️⃣',
#     4:'4️⃣',
#     5:'5️⃣'
# }
# from aiogram.fsm.context import FSMContext
# # Check Answers With Write by Hand
# @dp.message(F.text.startswith('#'))
# async def checkmytest(message:types.Message,state:FSMContext):
    
#         try:
#             answers = message.text
#             stuanswers = await checkformat(answers)
#             if stuanswers:
#                 test = stuanswers['test']
#                 answers = stuanswers['answers']
#                 trueanswers = await get_answers()
#                 if trueanswers == {}:
#                     await message.answer('<b>😐 Uzr bu kodli test sizga berilmagan!!</b>')
#                 else:
#                     result = await check(answers=answers, trueanswers=trueanswers.get('answers', {}))
#                     await done_test(
#                         code=trueanswers.get('code', 0),
#                         telegram_id=message.from_user.id,
#                         name=message.from_user.full_name,
#                         true_answers=result['trues'],
#                         false_answers=result['falses']
#                     )
#                     await message.answer(f"<b>‼️ Test kodi: {test}</b>\n\n{result['result']}")

#             else:
#                 await message.answer(error)
#             await state.clear()
#         except:
#             await state.clear()
 
# # Run When "Orqaga" or "Oldinga"
# @dp.callback_query(NextPreviousCallBack.filter())
# async def test(call:types.CallbackQuery,callback_data:NextPreviousCallBack,state:FSMContext):
#    try:
#        action = callback_data.action
#        data = await state.get_data()
#        answers = data.get('answers', {})
#        if action == 'next':
#            await call.message.edit_reply_markup(reply_markup=checkbuttonpart_2( answers=answers))
#        else:
#            await call.message.edit_reply_markup(reply_markup=checkbuttonpart_1(answers=answers))
#    except:
#        pass
# # Select clicked answers
# @dp.callback_query(CheckToCallBack.filter())
# async def write(call:types.CallbackQuery,callback_data:CheckToCallBack,state:FSMContext):
#     await call.answer("Iltimos javobni belgilang!")
# @dp.callback_query(CheckCallBack.filter())
# async def write(call:types.CallbackQuery,callback_data:CheckCallBack,state:FSMContext):
#     try:
#         await call.answer("Javob qabul qilindi!")
#         answer_number = callback_data.answer_number
#         answer = callback_data.answer
#         data = await state.get_data()
#         answers = data.get('answers', {})
#         answers[(answer_number)] = answer
#         await state.update_data({
#             'answers':answers
#         })
#         with suppress(TelegramBadRequest):
#             if int(answer_number) < 16:
#                 await call.message.edit_reply_markup(reply_markup=checkbuttonpart_1(answers=answers))
#             else:
#                 await call.message.edit_reply_markup(
#                     reply_markup=checkbuttonpart_2(answers=answers))
#     except Exception as e:
#         print(e)
#         pass
# # Run after click 'Tugatish'
# @dp.callback_query(FinishCallBack.filter())
# async def callme(call:types.CallbackQuery,state:FSMContext,callback_data:FinishCallBack):
#     try:
#         data = await state.get_data()
#         answers = data.get('answers', {})
#         myanswers = {}
#         for key,value in answers.items():
#             myanswers[str(key)]=value
#         trueanswers = await get_answers()
#         if trueanswers is None:
#             await call.answer('Javoblar kiritilmagan!')
#         if answers is None:
#             await call.answer('Javoblar kiritilmagan!')
#         else:
#             await call.answer(cache_time=60)
#             result = await check(trueanswers=trueanswers.get('answers',{}), answers=myanswers)
#             await call.message.answer(f"<b>‼️ Test kodi: { trueanswers.get('code')}</b>\n{result['result']}")
#             await done_test(
#                 code=trueanswers.get('code',0),
#                 telegram_id=call.from_user.id,
#                 name=call.from_user.full_name,
#                 true_answers=result['trues'],
#                 false_answers=result['falses']
#             )
#             await state.update_data({
#                 'answers': {}
#             })
#             await call.message.delete()
#     except:
#         pass
