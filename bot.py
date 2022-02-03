import logging

from aiogram import Bot, Dispatcher, executor, types

from googletrans import Translator
from oxford_qidiruvchi import getDefinition

translator = Translator()

API_TOKEN = '5127529271:AAEM9Tu08DlE4zogN-YZ1_8gDyIHYhfBZtE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom ushbu bot Ingliz va uzbek tilidagi jumlalarni tarjima qiladi\nAgar ingliz tilida 2 tagacha so'z kiritsaiz uning definitionini chiqaradi.")
    
@dp.message_handler()
async def tilmoch(message: types.Message):
# old style:
# await bot.send_message(message.chat.id, message.text)
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
        
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text
        
        izla = getDefinition(word_id)
        if izla:
            await message.reply(f"Word: {word_id} \nDefinitions: \n{izla['definitions']}")
            if izla.get('audio'):
                await message.reply_audio(izla['audio'])
        else:
            await message.reply("🤒  Bunday so'z topilmadi")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)