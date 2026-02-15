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
from write_sertificate import * 
def tekst(code,questions):
    tekst_=f"<b>✅Test bazaga qo`shildi.</b>\n"\
    f"<b>Test kodi: {code}</b>\n"\
    f"<b>Test turi: 🔍 Attestatsiya</b>\n"\
    f"<b>Savollar soni: {questions} ta.</b>\n"\
    f"<b>Quyidagi tayyor izohni o'quvchilaringizga yuborishingiz mumkin</b>\n"\
    f"<b>👇👇👇</b>\n"
    return tekst_
def tekst2(creator,questions,code,bot_username,user_id):  
    tekst_2 =  f"📝📝Test boshlandi.\n\n\n"\
    f"👤 Test muallifi:    {html.link(value=creator,link=f'tg://user?id={user_id}')}\n\n\n"\
    f"ℹ️ Test turi:🔍 Attestatsiya\n\n"\
    f"ℹ️ Savollar soni: {questions} ta\n\n\n"\
    f"ℹ️ Test kodi: {code}\n\n\n"\
    f"🔴 Javoblaringizni @{bot_username} ga quyidagi ko'rinishlarda yuborishingiz mumkin:\n\n"\
    f"{html.pre('++test_kodi++1a2b3c4d....50')}\n\n\n"\
    f"🛑 Eslatma!\t"\
    f"Javoblar aynan @{bot_username} ga yuborilishi shart, boshqasiga emas.\n"
    return tekst_2
    
# Check Answers With Write by Hand
@dp.message((F.text == "🔍 Attestatsiya test"))
async def attestat(message:types.Message,state:FSMContext):
     
           await message.answer(
              text=f"⬆️ Kerakli bo'limni tanlang.",
              reply_markup=test_button_attestat()  )
# Check Answers With Write by Hand
@dp.message((F.text =="➕ Attestatsiya test yaratish") )
async def attestat_create_test(message:types.Message,state:FSMContext):
           await message.answer(
               text=  f"<b>##1a2b3c4d....50b ko'rinishida test yarating.</b>\n\n",reply_markup=cancel_button()
           )
           await state.set_state(AttestatTestCreate.create)
from aiogram.types import ReplyKeyboardRemove
@dp.message((F.text.startswith('##') | (F.text=="🔙 Orqaga")),AttestatTestCreate.create )
async def attestat_create_test(message:types.Message,state:FSMContext):
        text = message.text
        if text =="🔙 Orqaga":
            await message.answer(
              text=f"⬆️ Kerakli bo'limni tanlang.",
              reply_markup=main_button()  )
            await state.clear()
        else:
            info = await checkformat(text)
            if info:
                telegram_id = message.from_user.id 
        
            type='attestat'
            answers = info.get('answers_string',None)
            me = await bot.get_me()
            bot_username = me.username
            created = await create_answers(
                telegram_id=telegram_id,
                answers=answers,
                type_test=type
            )
            await message.answer(
                tekst(
                    code = created,
                    questions=info.get('len',None)
                ),
                reply_markup=test_button_back()
            )
            await message.answer(
                html.bold(
                    tekst2(
                    code = created,
                    questions=info.get('len',None),
                    user_id=message.from_user.id,
                    creator=message.from_user.full_name,
                    bot_username=bot_username
                    
                )
                ),
                reply_markup=test_button_back()
            )            
            await state.clear()
           
# Check 
@dp.message((F.text =="✅ Attestatsiya testini tekshirish") )
async def attestat_check_test(message:types.Message,state:FSMContext):
           matn = f"🔴 Javoblaringizni  quyidagi ko'rinishlarda yuborishingiz mumkin:\n\n"\
           f"{html.pre('++test_kodi++1a2b3c4d....50b')}\n\n\n"\
           
           await message.answer(matn)
from aiogram.types import ReplyKeyboardRemove
@dp.message((F.text.startswith('++')))
async def attestat_check_test(message:types.Message,state:FSMContext):
            
            info = await checkformat_1(message.text)
            if info:
                val = "☝️ To'g'ri test yakunlangandan so'ng yuboriladi."
                code  = info.get('test_code',None)
                get_test_me = await get_test(id=code)
                done = await done_or_not(code=code,telegram_id=message.from_user.id)
                if done:
                    await message.answer(html.bold('Siz,bu testni allaqachon bajardingiz!'))
                else:
                    if get_test_me.get('answers',None):
                        info_2 = await checkformat_1(f"++{get_test_me['code']}++{get_test_me['answers']}")
                        data = await check_answers(
                            trueanswers=info_2['answers'],answers=info['answers']
                        )
                        await message.answer(f"{html.bold('👤 Foydalanuvchi: ')}\n\n"\
                            f"{html.bold(html.link(value=f'{message.from_user.full_name}',link=f'tg://user?id={message.from_user.id}'))}\n\n"\
                            f"{html.bold(f'📖 Test kodi: {code}')}\n" \
                            f"{data['result']}\n\n\n\n\n\n"\
                            f"<b>'🎉🎉🎉</b>'{html.bold(value=data['level'])}\n\n\n\n\n" \
                            f"{html.bold(value=val)}" 
                                
                        )
                        await message.answer(html.bold(data['text_']),reply_markup=ReplyKeyboardRemove())
                        await create_results(
                            code = code,
                            name = message.from_user.full_name,
                            trues=data['trues'],
                            falses=data['falses'],
                            telegram_id=message.from_user.id,
                        )
                        try:
                            cont =  f"{html.bold(html.link(value=f'{message.from_user.full_name}',link=f'tg://user?id={message.from_user.id}'))} {html.bold(code)} kodli testning javoblarini yubordi.\n\n"\
                                    f"Natijasi: {html.bold(data['trues'])} ta to'g'ri va {html.bold(data['falses'])} ta noto'g'ri\n\n"\
                                    f"/joriyholat_{code}\n"\
                                    f"/yakunlash_{code}"
                            await bot.send_message(
                                chat_id=get_test_me.get('telegram_id'),
                                text= cont,
                                reply_markup=ReplyKeyboardRemove()
                            )
                        except:
                            pass
                    else: 
                             pass
                
            else:
                
                matn = f"🔴 Javoblaringizni  quyidagi ko'rinishlarda yuborishingiz mumkin:\n\n"\
           f"{html.pre('++test_kodi++1a2b3c4d....30b')}\n\n\n"\
           
                await message.answer(matn)

@dp.message(F.text.startswith('/joriyholat'))
async def start_handler(message: Message):
    parts = message.text.split("_", 1)
    code = parts[1]
    data = await get_results(code=code)
    test = await get_test(id=code)
    telegram_id_=test.get('telegram_id',None)
    sorted_data = sorted(data, key=lambda x: int(x['trues']), reverse=True)
    text_me = ''
    counter_=1
    for i in sorted_data:
        name = i.get('name',None)
        telegram_id = i.get('telegram_id',None)
        text_me+=f"{counter_}.{html.bold(html.link(value=f'{name}',link=f'tg://user?id={telegram_id}'))}\n"
        counter_+=1
    context = f"📊 Natijalarning joriy holati.\n\n"\
              f"{html.link(value='Test Muallifi',link=f'tg://user?id={telegram_id_}')}\n\n"\
              f"✅ Natijalar:\n\n"\
              f"{text_me}"   


    await message.answer(html.bold(context))
@dp.message(F.text.startswith('/yakunlash'))
async def start_handler(message: Message):
    try:
        parts = message.text.split("_", 1)
        code = parts[1]
        data = await get_results(code=code)
        test = await get_test(id=code)
        telegram_id_=test.get('telegram_id',0)
        if int(telegram_id_) == message.from_user.id:
            user = await get_user(telegram_id=int(telegram_id_))
            
            try:
                author = user.get('name',None)
                channel = user.get('guruh','@Korgazmali_talim')
            except:
                author = 'None'
                channel = '@Korgazmali_talim'
            sorted_data = sorted(data, key=lambda x: int(x['trues']), reverse=True)
            text_me = ''
            counter_=1
            for i in sorted_data:
                get_result = await done_or_not(code=code,telegram_id=i['telegram_id'])
                true_ = int(get_result.get('trues',1))
                false_=int(get_result.get('falses',1))
                degree__ = await info_degree_(all=true_+false_,trues=true_)
                if degree__:
                    name = i.get('name',None)
                    telegram_id = i.get('telegram_id',None)
                    text_me+=f"{counter_}.{html.bold(html.link(value=f'{name}',link=f'tg://user?id={telegram_id}'))}  ---  {html.bold(degree__)}\n"
                    counter_+=1
                else:
                    name = i.get('name',None)
                    telegram_id = i.get('telegram_id',None)
                    text_me+=f"{counter_}.{html.bold(html.link(value=f'{name}',link=f'tg://user?id={telegram_id}'))}\n"
                    counter_+=1
                    
            data_me = await checkformat_2(javoblar=test['answers'])
            te_= await show_answers(data_me)
            
            context = f"⛔️Test yakunlandi.\n\n"\
                    f"{html.link(value='Test Muallifi',link=f'tg://user?id={telegram_id_}')}\n\n"\
                    f"✅ Natijalar:\n\n"\
                    f"{text_me}\n\n\n"\
                    f"To`g`ri javoblar:\n\n"\
                    f"{html.pre(te_)}"  
            for i in data:
                try:    
                        get_result = await done_or_not(code=code,telegram_id=i['telegram_id'])
                        true_ = int(get_result.get('trues',1))
                        false_=int(get_result.get('falses',1))
                        degree__me = true_*100 / (true_+false_)
                        score = "{:.2f}".format(degree__me)
                        student =await get_user(int(i['telegram_id']))
                        student_ = student.get('name','None')
                except:
                        student_ ='None'
                        true_ = int(get_result.get('trues',1))
                        false_=int(get_result.get('falses',1))
                        degree__me = true_*100 / (true_+false_)
                        score = "{:.2f}".format(degree__me)
               
                await bot.send_message(
                    
                    text=html.bold(context),
                    chat_id=i['telegram_id'],
                     reply_markup=test_button_back()
                )
          
                try:
                    from aiogram.types import BufferedInputFile
                    image_bytes = write_attestat_image(author=author,student=student,degree=score,channel=channel)
                    photo = BufferedInputFile(
                    image_bytes.read(),
                    filename="image.png"
        )
                    await bot.send_photo(photo=photo, chat_id=i['telegram_id'])
                except:
                    pass
                await delete_result_(code=int(code))
                await delete_answer_(id=code)
                
        else:
            await message.answer(html.bold('Siz bu testni yakunlay olmaysiz!'))
        #await message.answer(html.bold(context))
    except TelegramBadRequest as e:
        if "message is too long" in str(e):
            parts = message.text.split("_", 1)
            code = parts[1]
            data = await get_results(code=code)
            test = await get_test(code=code)
            telegram_id_=test.get('telegram_id',None)
            sorted_data = sorted(data, key=lambda x: int(x['trues']), reverse=True)
            text_me = ''
            counter_=1
            for i in sorted_data:
                name = i.get('name',None)
                telegram_id = i.get('telegram_id',None)
                text_me+=f"{counter_}.{html.bold(html.link(value=f'{name}',link=f'tg://user?id={telegram_id}'))}\n"
                counter_+=1
            data_me = await checkformat_2(javoblar=test['answers'])
            te_= await show_answers(data_me)
            
            context = f"⛔️Test yakunlandi.\n\n"\
                    f"{html.link(value='Test Muallifi',link=f'tg://user?id={telegram_id_}')}\n\n"\
                    f"✅ Natijalar:\n\n"\
                    f"{text_me}\n\n\n"\
                    f"To`g`ri javoblar:\n\n"\
                    f"{html.pre(te_)}" 
            MAX_LEN = 4096      
            parts = []
            while context:
                parts.append(context[:MAX_LEN])
                context = context[MAX_LEN:]

            for part in parts:
                for i in data:
                    await bot.send_message(
                        text=html.bold(part),
                        chat_id=i['telegram_id']
                    )     
                #await message.answer(html.bold(part))
            await delete_result_(code=int(code))
            await delete_answer_(id=code)
        else:
            raise e
