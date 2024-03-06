from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def confirm_kb() -> ReplyKeyboardBuilder:
    kb = InlineKeyboardBuilder()
    kb.button(text='Принять заявку', callback_data=f'confirm')
    kb.button(text='Отклонить заявку', callback_data=f'cancel')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)

