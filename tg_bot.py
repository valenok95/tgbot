import json

from aiogram import Bot, Dispatcher, executor, types

import main
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)


#@dp.message_handler(commands="start")
#async def start(message: types.Message):
#    await message.reply("What's up Doc?")


@dp.message_handler(commands="check")
async def check_first_price(message: types.Message):
    #main.get_first_price()
    await message.reply(main.get_first_price())

if __name__ == '__main__':
    executor.start_polling(dp)
