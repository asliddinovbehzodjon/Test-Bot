import handlers,middlewares
from loader import dp,bot,db
import asyncio
from utils.notify_admins import start,shutdown

# Info
import logging
from utils.set_bot_commands import private_chat_commands
from middlewares.mymiddleware import UserCheckMiddleware
import sys
async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await private_chat_commands()
        dp.startup.register(start)
        dp.shutdown.register(shutdown)
        dp.message.middleware(UserCheckMiddleware())
        try:
            db.create_table_results()
            db.create_table_users()
            db.create_table_channels()
            db.create_table_answers()
        except Exception as e:
            print(e)
            pass
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
if __name__=='__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())