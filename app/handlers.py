from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import app.keyboards as keyboard


router = Router()

@router.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer('''🏃‍♂️ Добро пожаловать в RunRankBot!
Я помогу узнать актуальные разряды по лёгкой атлетике.
Выберите действие:''', reply_markup=keyboard.main_menu)