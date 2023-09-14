from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text

from config import BOT_TOKEN
from constants import IMPORT_CHAT_ID, EXPORT_CHAT_ID, BOT_NAME
from bot_commands import COMMAND_FILTER
from model.table import update_table
from view.text import generate_answer

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)


@dp.message_handler(Text(equals=COMMAND_FILTER), chat_id=IMPORT_CHAT_ID)
async def say_hello(message: types.Message):
	m_text = message.text.split('@')[0] if BOT_NAME in message.text else message.text
	user_id = message.from_user.id
	full_name, old_value, new_value = update_table(user_id, m_text)
	text = generate_answer(full_name, m_text, old_value, new_value)
	await bot.send_message(EXPORT_CHAT_ID, text=text)


@dp.message_handler(commands=['check'])
async def say_hello(message: types.Message):
	user_id = message.from_user.id
	chat_id = message.chat.id
	text = (f'{user_id=}\n'
			f'{chat_id=}')
	await message.answer(text)


if __name__ == '__main__':
	executor.start_polling(dp)
