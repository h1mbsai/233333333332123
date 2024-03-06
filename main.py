import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import TOKEN
from core.handlers import basic, questionaire, adminpanel
from core.db import database as db

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


async def on_startup():
    await db.db_start()
    

async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(
        basic.router,
        questionaire.router,
        adminpanel.router,
    )
    
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    loop = asyncio.get_event_loop() #создание ассинхронного потока для работы бд 
    loop.run_until_complete(on_startup()) #запуск бд
    
    try:
        asyncio.run(main()) # запуск бота
    except KeyboardInterrupt:
        print('Exit')
