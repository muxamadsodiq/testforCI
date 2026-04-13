import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Bot tokeningni bu yerga qo'yasan
TOKEN = "7018329872:AAGfELzfqDfXjfkejfjiE0hdC_AeXsByJRk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Har qanday xabarga javob berish (Echo)
@dp.message()
async def echo_handler(message: types.Message):
    # Sen aytgan birinchi holat: nima yozsa, o'zini qaytaradi
    await message.answer(message.text)

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())