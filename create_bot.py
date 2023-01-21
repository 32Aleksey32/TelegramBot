import os

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv

storage = MemoryStorage()

load_dotenv()

secret_token = os.getenv('TOKEN')

bot = Bot(token=secret_token)

dp = Dispatcher(bot, storage=storage)
