# Admin Button
from aiogram.utils.keyboard import ReplyKeyboardBuilder,KeyboardButton
def admin_button():
    button = ReplyKeyboardBuilder()
    button.row(

        KeyboardButton(text="📊 Obunachilar soni"),
                   KeyboardButton(text="🗣 Kanal qo'shish")

    )
    button.row(
               KeyboardButton(text="🗣 Kanallar"),
               KeyboardButton(text="❌ Kanal o'chirish"))

    button.adjust(2,2)
    return button.as_markup(resize_keyboard=True,one_time_keyboard=True,input_field_placeholder="Kerakli bo'limni tanlang!")
def add_type():
    button = ReplyKeyboardBuilder()
    button.row(
        KeyboardButton(text="📝 Tekst"),
        KeyboardButton(text="📸 Rasm")
    )
    button.row(
        KeyboardButton(text="🎞 Video"),
        KeyboardButton(text="⬅️ Orqaga")
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def back_button():
    button = ReplyKeyboardBuilder()

    button.row(

        KeyboardButton(text="◀️ Orqaga")
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def need_or_not():
    button = ReplyKeyboardBuilder()

    button.row(
        KeyboardButton(text="⏺ Bekor qilish"),
        KeyboardButton(text="🆗 Kerakmas")
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def send():
    button = ReplyKeyboardBuilder()

    button.row(
        KeyboardButton(text="⏺ Bekor qilish"),
        KeyboardButton(text="📤 Yuborish")
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def choose_role():
    button = ReplyKeyboardBuilder()

    button.row(
        KeyboardButton(text="🧑‍🏫 O'qituvchi"),
        KeyboardButton(text="🧑‍🎓 O'quvchi"),
        KeyboardButton(text='📚 Repetitor')
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def main_button():
    button = ReplyKeyboardBuilder()

    button.row(
        KeyboardButton(text="🔍 Attestatsiya testlari"),
        KeyboardButton(text="🧮 Testlar"),
        KeyboardButton(text="🏫 Maktab testlari"),
        KeyboardButton(text='🪪 Mening ma’lumotlarim'),
        KeyboardButton(text="🤖 Bot haqida ma’lumot"),
        KeyboardButton(text="Sertifikat tanlash")
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def change_info_button(role):
    button = ReplyKeyboardBuilder()
    if role:
        button.row(
            KeyboardButton(text="🔄 Ism-familyani o'zgartirish"),
            KeyboardButton(text="ℹ️ Faoliyat turini o'zgartirish"),
            KeyboardButton(text="🔗 Kanalni o'zgartirish"),
            KeyboardButton(text="⬅️ Orqaga"),
          
        )
        button.adjust(2)
        return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
    else:
        button.row(
            KeyboardButton(text="🔄 Ism-familyani o'zgartirish"),
            KeyboardButton(text="ℹ️ Faoliyat turini o'zgartirish"),
            KeyboardButton(text="⬅️ Orqaga"),
            
           
        )
        button.adjust(2)
        return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def test_button_attestat():
    button = ReplyKeyboardBuilder()
   
    button.row(
        KeyboardButton(text="➕ Attestatsiya Testi Yaratish"),
        KeyboardButton(text="✅ Attestatsiya Testini tekshirish"),
        KeyboardButton(text="⬅️ Orqaga"),
        
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def test_button_school():
    button = ReplyKeyboardBuilder()
   
    button.row(
        KeyboardButton(text="➕ Maktab Testi Yaratish"),
        KeyboardButton(text="✅ Maktab Testini tekshirish"),
        KeyboardButton(text="⬅️ Orqaga"),
        
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def test_button_simple():
    button = ReplyKeyboardBuilder()
   
    button.row(
        KeyboardButton(text="➕ Test Yaratish"),
        KeyboardButton(text="✅ Testni tekshirish"),
        KeyboardButton(text="⬅️ Orqaga"),
        
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def cancel_button():
    button = ReplyKeyboardBuilder()
   
    button.row(
        KeyboardButton(text="❌ Bekor qilish"),
        
        
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
