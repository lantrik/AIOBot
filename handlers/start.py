from src.core import Bot

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from src.ext.keyboards import problem_keyboard


router = Router()

@router.message(Command(commands=["start"]))
async def start_command(message: Message) -> None:
    await message.answer("Привет!")

    await message.answer("Для начала, можешь выбрать одну из тем, которые тебя беспокоят? 😣")

    await message.answer(
        "Главное — помни, что не только ты можешь столкнуться с трудностями, они бывают у всех.",
        reply_markup=problem_keyboard()
        )
