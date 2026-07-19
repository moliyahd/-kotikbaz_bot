import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👩 Обо мне")],
        [KeyboardButton(text="📖 Моя история")],
        [KeyboardButton(text="💚 Помощь")],
        [KeyboardButton(text="📩 Контакты")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет! 👋\nЯ бот Молли.\nВыбери раздел ниже.",
        reply_markup=menu
    )

@dp.message(F.text == "👩 Обо мне")
async def about(message: Message):
    await message.answer("Меня зовут Молли. Здесь ты можешь узнать обо мне.")

@dp.message(F.text == "📖 Моя история")
async def story(message: Message):
    await message.answer("Здесь будет моя история.")

@dp.message(F.text == "💚 Помощь")
async def help_cmd(message: Message):
    await message.answer("Я всегда постараюсь поддержать и помочь.")

@dp.message(F.text == "📩 Контакты")
async def contacts(message: Message):
    await message.answer("Здесь будут мои контакты.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
