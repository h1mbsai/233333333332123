from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from core.keyboards.start_kb import start_kb, questionare_start_kb
from core.keyboards.back_keybaord import back_discord, back_kb
from config import ADMIN_IDS
from core.db import database as db

router = Router()


@router.message(CommandStart())
async def get_start(message: Message):
    await db.cmd_start_db(message.from_user.id)
    await message.answer(f'<b>Здравствуйте, {message.from_user.first_name}👋\nПожалуйста, выберите действие:</b>', reply_markup=start_kb(telegram_id=message.from_user.id)) #отправка в тот чат, в котором написал user

@router.message(F.text.lower() == 'про нас')
async def answer_about_us(message: Message):
    await message.answer(f'<b>Привет, мы - Marmeladov clxn!\nМы играем на сервере Majestic (San Francisco, 04)\nЦель нашего клана, не только выбивать хевики и жить этим, как это делают наши конкуренты, а собрать классный стак ребят, которые дружат с друг другом и помогают друг другу.\nМы так же известны как: Bedolagov SQUAD, MAGOMEDOFF CLXN.\nУ нас своя функциональная семья, дом, вертолёт и всё, что нужно для плотного хасана на складе.\nЯ уверен что ты подходишь нам, оставляй заявку!</b>', reply_markup=back_kb())

@router.message(F.text.lower() == 'наши контакты')
async def answer_contact(message: Message):
    await message.answer(f'<b>Наш дискорд (по кнопке ниже)\nСвязь в телеграмм с главным админом бота - @h1mbsai</b>', reply_markup=back_discord())

@router.message(F.text.lower() == 'оставить заявку')
async def answer_zayavka(message: Message):
    await message.answer(f'<b>Для создания заявки нажмите на кнопку ниже:</b>', reply_markup=questionare_start_kb())

@router.message(F.text.lower() == 'админ. панель')
async def answer_zayavka(message: Message):
    if message.from_user.id in ADMIN_IDS:
        await message.answer(f'<b>Админ панель:</b>', reply_markup=back_kb())
    else:
        await message.answer(f'<b>У Вас нет доступа</b>')

@router.callback_query(F.data == 'start')
async def back(call: CallbackQuery):
    await call.message.answer('<b>Выберите действие:</b>', reply_markup=start_kb(telegram_id=call.from_user.id))