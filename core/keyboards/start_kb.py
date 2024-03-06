from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import KeyboardBuilder, ReplyKeyboardBuilder, InlineKeyboardBuilder

from config import ADMIN_IDS


def start_kb(telegram_id) -> ReplyKeyboardBuilder:
    kb = KeyboardBuilder(button_type=KeyboardButton)
    kb.button(text='Оставить заявку')
    kb.button(text='Про нас')
    kb.button(text='Наши контакты')
    if telegram_id in ADMIN_IDS:
        kb.button(text='Админ. Панель')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)

def questionare_start_kb() -> ReplyKeyboardBuilder:
    kb = InlineKeyboardBuilder()
    kb.button(text='Создать заявку',callback_data='profile')
    kb.button(text='Назад',callback_data='start')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
