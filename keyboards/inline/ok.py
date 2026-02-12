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
