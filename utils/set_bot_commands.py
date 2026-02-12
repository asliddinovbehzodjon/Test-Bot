from aiogram import types,html
from loader import bot
from aiogram.types.bot_command_scope_all_private_chats import BotCommandScopeAllPrivateChats
async def private_chat_commands():
    commands = [
        types.BotCommand(command='start', description="🔄 Botni ishga tushirish"),
        types.BotCommand(command='help', description="🆘 Testni tekshirish haqida"),

    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeAllPrivateChats(type='all_private_chats')
    )