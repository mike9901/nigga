import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6955144667:AAExRG4ghxYDysrW-Hh-pSvENjwRN0m9-WQ")
# Диспетчер
dp = Dispatcher()

@dp.message(Command("start"))
async def my_start(message: types.Message):
    await message.answer("Hello")

@dp.message(Command("button"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Кнопка 1"), types.KeyboardButton(text="Кнопка 3")],
        [types.KeyboardButton(text="Кнопка 2")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Вибери кнопку", reply_markup=keyboard)

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message, bot: Bot):
    await bot.send_dice(message.chat.id, emoji=DiceEmoji.BASKETBALL)

@dp.message(F.text)
async def echo_message(message: types.Message):
    if message.text == "Кнопка 1":
        await message.answer("Ти натиснув на кнопку 1")
    await message.answer(message.text)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())