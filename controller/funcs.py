from aiogram import types

from controller.initialize import bot, logger

from constants import EXPORT_CHAT_ID

from model.table import update_table
from view.text import generate_answer, generate_error_message


async def main(message: types.Message):
	try:
		m_text = message.text.split('@')[0]  # delete bot name from command

		user_id = message.from_user.id
		full_name, old_value, new_value = update_table(user_id, m_text)

		text = generate_answer(full_name, m_text, old_value, new_value)
	except KeyError as err_message:
		error_message = generate_error_message('KeyError', err_message, message)
		logger.error(error_message)
	else:
		await bot.send_message(EXPORT_CHAT_ID, text=text)


async def check_id(message: types.Message):
	user_id = message.from_user.id
	chat_id = message.chat.id
	text = (f'{user_id=}\n'
			f'{chat_id=}')
	await message.answer(text)


start_bot_message = lambda x: bot.send_message(EXPORT_CHAT_ID, 'Бот запущен')
shutdown_bot_message = lambda x: bot.send_message(EXPORT_CHAT_ID, 'Бот остановлен')
