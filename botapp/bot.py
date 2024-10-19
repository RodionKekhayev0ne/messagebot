# mybot/bot.py
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from asgiref.sync import sync_to_async
from django.utils import timezone

from asgiref.sync import sync_to_async

from botapp.models import Application

API_TOKEN = '7835737111:AAFLRUhLbAZeMGuQq6jZUk7nWFwKh8egJFM'  # Замените на ваш токен

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот на aiogram 3.x и Django.")


@dp.message()
async def handle_message(message: types.Message):
    user_message = message.text  # Получаем текст сообщения от пользователя
    user = message.from_user
    person_dt = user.username
    if person_dt is None:
        person_dt = user.first_name + " " + user.last_name

    application = Application(description=user_message, person=person_dt)
    await sync_to_async(application.save)()
    await message.answer("Ваша заявка расмотренна")


async def start_bot():
    await dp.start_polling(bot)
