from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def back_kb() -> ReplyKeyboardBuilder:
    kb = InlineKeyboardBuilder()
    kb.button(text='Назад',callback_data='start')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)

def back_discord() -> ReplyKeyboardBuilder:
    kb = InlineKeyboardBuilder()
    kb.button(text='Discord', url='https://discord.gg/GgAP9e74cv')
    kb.button(text='Назад',callback_data='start')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)

