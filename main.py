from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text

import pygsheets

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
client = pygsheets.authorize(service_account_file='service.json')

sheet = client.open('NG Bedarev - SALES ONLINE')
worksheet = sheet.sheet1

dp = Dispatcher(bot=bot)

imp = -4058772368
exp = -4005445058


def get_names():
	data = worksheet.get_values('A', 'C')
	data = list(filter(lambda x: x[1] != '', data))
	id_name = {}
	for element in data:
		id_name[element[1]] = (element[2], element[0])
	return id_name


@dp.message_handler(Text(equals=['/combo', '/bs', '/cp', '/selfie',
								 '/combo@AlfaBank_staff_Bot', '/bs@AlfaBank_staff_Bot',
								 '/cp@AlfaBank_staff_Bot', '/selfie@AlfaBank_staff_Bot']), chat_id=imp)
async def say_hello(message: types.Message):
	m_text = message.text.split('@')[0] if '@AlfaBank_staff_Bot' in message.text else message.text
	user_id = message.from_user.id
	id_names = get_names()
	name, number = id_names[str(user_id)]
	surname, name, *second_name = name.split()
	data = {'/combo': 'D', '/bs': 'E', '/cp': 'F', '/selfie': 'G'}
	col = data[m_text]
	old_value = worksheet.cell(f'{col}{number}').value
	new_value = int(old_value) + 1 if old_value != '' else 1
	worksheet.update_value(f'{col}{number}', f'{new_value}')
	text = (f"""Фамилия: {surname}\n"""
			f"""Имя: {name}\n"""
			f"""Отчество: {" ".join(second_name)}\n"""
			f"""Сообщение: {m_text}\n"""
			f"""Изменения в таблице: {old_value if old_value != "" else 0} -> {new_value}""")
	await bot.send_message(exp, text=text)


@dp.message_handler(commands=['check'])
async def say_hello(message: types.Message):
	user_id = message.from_user.id
	chat_id = message.chat.id
	print(message)
	text = (f'user id = {user_id}\n'
			f'chat id = {chat_id}')
	await message.answer(text)


if __name__ == '__main__':
	executor.start_polling(dp)
