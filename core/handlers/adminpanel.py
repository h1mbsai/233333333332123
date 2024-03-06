from config import TOKEN

from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery
from aiogram.enums import ParseMode

from core.keyboards.invite_keyboard import invite_kb

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


router = Router()


@router.callback_query(F.data == 'confirm')
async def back(call: CallbackQuery):
    user_id = call.from_user.id
    await bot.send_message(user_id, f"<b>Ваша заявка принята!\nДобро пожаловать в стак 🎉\nВсе нужные инвайты:</b>", reply_markup=invite_kb)

@router.callback_query(F.data == 'cancel')
async def back(call: CallbackQuery):
    user_id = call.from_user.id
    await bot.send_message(user_id, '<b>Вам пришёл ответ от администратора:\nК сожалению, вы нам не подходите, попробуйте оформить заявку ещё раз, возможно, от вас поступило слишком мало информации.</b>')
