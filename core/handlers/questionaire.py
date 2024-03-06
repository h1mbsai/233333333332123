from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from core.utils.states import Form
from core.keyboards.builders import profile
from core.keyboards.confirm_keyboard import confirm_kb

from main import bot
from config import ADMIN_IDS


rmk = ReplyKeyboardRemove()

router = Router()


@router.callback_query(F.data == 'profile')
async def fill_profile(call: CallbackQuery, state: FSMContext):
    await state.set_state(Form.name)
    await call.message.answer(
        f"<b>Давай начнем, введи свое имя:</b>",
        reply_markup=profile(call.from_user.first_name)
    )


@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.update_data(tg_id=message.from_user.id) 
    await state.set_state(Form.age)
    await message.answer(f"<b>Отлично, теперь введи свой возраст:</b>")


@router.message(Form.age)
async def form_age(message: Message, state: FSMContext):
    if message.text.isdigit():
        age = int(message.text)
        if age <= 99:
            await state.update_data(age=age)
            await state.set_state(Form.experience)
            await message.answer(
                f"<b>Что насчёт опыта? Был ли ты в подобных стаках?</b>",
                reply_markup=profile(["Да, был", "Нет, не был"])
            )   
        else:
            await message.answer(f"<b>Пожалуйста, введите ваш настоящий возраст ⚠️</b>")
    else:
        await message.answer(f"<b>Неверный тип данных. Пожалуйста, введите числовое значение для возраста ⚠️</b>")

@router.message(Form.experience, F.text.casefold().in_(["да, был", "нет, не был"]))
async def form_experience(message: Message, state: FSMContext):
    await state.update_data(experience=message.text)
    await state.set_state(Form.about)
    await message.answer(f"<b>Почти закончили. Расскажи о себе, в каких стаках ты был, как давно играешь? В конце укажи свой discord для связи!</b>", reply_markup=rmk)


@router.message(Form.experience)
async def incorrect_form_experience(message: Message, state: FSMContext):
    await message.answer("Нажми на кнопку")


@router.message(Form.about)
async def form_about(message: Message, state: FSMContext):
    if len(message.text) < 5:
        await message.answer(f"<b>Ёу, слишком мало инфы, так ты точно не пройдёшь. Напиши о себе подробно, это очень важно!</b>")
    else:
        await state.update_data(about=message.text)
        await state.update_data(tg_id=message.from_user.id) 
        await state.set_state(Form.photo)
        await message.answer(f"<b>Последний шаг. Пришли фотографию своих игровых документов скриншотом.\nP.S. Это важно, тк нам необходимо знать ваш игровой никнейм и статик</b>")


@router.message(Form.photo, F.photo)
async def form_photo(message: Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    data = await state.get_data()
    await state.clear()

    formatted_text = []
    [
        formatted_text.append(f"{key}: {value}")
        for key, value in data.items()
    ]

    for admin_id in ADMIN_IDS:
        await bot.send_photo(
            admin_id,
            photo_file_id,
            caption="\n".join(formatted_text),
            reply_markup=confirm_kb()
        )

    await message.answer(f"<b>Анкета успешно отправлена. Спасибо!🔥\nОжидайте сообщения от администрации</b>")


@router.message(Form.photo, ~F.photo)
async def incorrect_form_photo(message: Message, state: FSMContext):
    await message.answer('<b>Не понимаю тип данных, пожалуйста, отправьте скриншот в формате картинки\n(Не убирайте галочку "Сжать фото")</b>')
