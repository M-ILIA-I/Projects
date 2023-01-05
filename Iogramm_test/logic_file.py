import asyncio
from aiogram import Bot, Dispatcher, executor, types
from main import get_text

api_token = "5678442450:AAGJkbV1Rgt60tb7JGFA6Ltkrp5R_4iql4A"
bot = Bot(token=api_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    start_buttons = ["/monitoring", "just button"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Monitoring is started", reply_markup=keyboard)


@dp.message_handler(commands=["monitoring"])
async def monitoring(message: types.Message):
    while True:
        text = get_text("https://v-minsk.com/Маршруты/Минск/Городок?date=2022-11-04&passengers=1&from=c625144&to=c628155")
        if text != "Нет мест":
            await message.answer("Реще заказывай билет...")
            break
    await asyncio.sleep(10)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

