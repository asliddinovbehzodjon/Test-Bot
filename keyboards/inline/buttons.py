from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
class Format(CallbackData,prefix='ikb0000'):
    choose:str
class FinishCallBack(CallbackData,prefix='ikb0003'):
   finish:bool
class CheckToCallBack(CallbackData,prefix='ikb00256'):
    check:bool
class CheckCallBack(CallbackData,prefix='ikb0004'):
    answer_number:int
    answer:str
class NextPreviousCallBack(CallbackData,prefix='ikb0005'):
    action:str

# Button for check (1-15)
def checkbuttonpart_1(answers:dict=None):
    btn = InlineKeyboardBuilder()
    for i in range(1,16):
                if answers is  None:
                    answer=None
                else:
                    answer = answers.get(int(i))
                try:

                    btn.row(
                        InlineKeyboardButton(text=f"{i}", callback_data=CheckToCallBack(check=True).pack()),
                        InlineKeyboardButton(text="✅ A" if answer == "A" else "A",
                                             callback_data=CheckCallBack( answer_number=i,
                                                                         answer="A").pack()),
                        InlineKeyboardButton(text="✅ B" if answer == "B" else "B",
                                             callback_data=CheckCallBack(
                                                                         answer_number=i, answer="B").pack()),
                        InlineKeyboardButton(text="✅ C" if answer == "C" else "C",
                                             callback_data=CheckCallBack(answer_number=i,
                                                                         answer="C").pack()),
                        InlineKeyboardButton(text="✅ D" if answer == "D" else "D",
                                             callback_data=CheckCallBack(
                                                                         answer_number=i, answer="D").pack()),
                        width=5

                    )
                except Exception as e:
                    print(e)
    # btn.adjust(5)
    btn.row(
        InlineKeyboardButton(text="➡️ Oldinga", callback_data=NextPreviousCallBack(action='next').pack())
    )
    return btn.as_markup()
# Buttot for check (16-30)
def checkbuttonpart_2(answers=None):
    btn = InlineKeyboardBuilder()
    for i in range(16,31):
        if answers is None:
            answer = None
        else:
            answer = answers.get(int(i))
        try:

            btn.row(
                InlineKeyboardButton(text=f"{i}", callback_data='1'),
                InlineKeyboardButton(text="✅ A" if answer == "A" else "A",
                                     callback_data=CheckCallBack( answer_number=i,
                                                                 answer="A").pack()),
                InlineKeyboardButton(text="✅ B" if answer == "B" else "B",
                                     callback_data=CheckCallBack(
                                                                 answer_number=i, answer="B").pack()),
                InlineKeyboardButton(text="✅ C" if answer == "C" else "C",
                                     callback_data=CheckCallBack( answer_number=i,
                                                                 answer="C").pack()),
                InlineKeyboardButton(text="✅ D" if answer == "D" else "D",
                                     callback_data=CheckCallBack(
                                                                 answer_number=i, answer="D").pack()),
                width=5

            )
        except Exception as e:
            print(e)
    btn.row(
       InlineKeyboardButton(text="⬅️ Orqaga", callback_data=NextPreviousCallBack(action='previous').pack())
    )
    btn.row(
        InlineKeyboardButton(text="🏁 Tugatish",callback_data=FinishCallBack(finish=True).pack())
    )
    return btn.as_markup()

def text_format(choose=None):
    choose = 'TEXT' if choose==None else choose
    btn  = InlineKeyboardBuilder()
    btn.button(text=f"Markup format: {choose}",callback_data=Format(choose=choose))
    return btn.as_markup()
from aiogram.filters.callback_data import CallbackData

class ItemCallback(CallbackData, prefix="sertificate"):
    name: str
    author:str
    channel:str
    degree:str
   
def button_sertificate_attestat(name,author,channel,degree):
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📜 Sertifikatni yuklab olish",
                    callback_data=ItemCallback(name=name,author=author,degree=degree,channel=channel).pack()
                ),
               
            ]
        ]
    )
    return keyboard
class SchoolCallback(CallbackData, prefix="schol"):
    name: str
    author:str
    degree:str
    subject:str
    class_number:str
   
def button_sertificate_school(name,author,degree,subject,class_number):
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📜 Sertifikatni yuklab olish",
                    callback_data=SchoolCallback(name=name,author=author,degree=degree,subject=subject,class_number=class_number).pack()
                ),
               
            ]
        ]
    )
    return keyboard
class SimpleCallback(CallbackData, prefix="simple"):
    name: str
    author:str
    degree:str
    
   
def button_sertificate_simple(name,author,degree):
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📜 Sertifikatni yuklab olish",
                    callback_data=SimpleCallback(name=name,author=author,degree=degree).pack()
                ),
               
            ]
        ]
    )
    return keyboard