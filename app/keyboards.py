from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

main_menu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Поиск нормативов'), KeyboardButton(text='Какой у меня разряд?')],
        [KeyboardButton(text='Помощь')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие...'
)