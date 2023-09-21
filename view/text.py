from aiogram import types


def generate_answer(full_name: str, message_text: str, old_value: int, new_value: int) -> str:
	surname, name, *second_name = full_name.split()
	text = (f"""Фамилия: {surname}\n"""
			f"""Имя: {name}\n"""
			f"""Отчество: {" ".join(second_name)}\n"""
			f"""Сообщение: {message_text}\n"""
			f"""Изменения в таблице: {old_value} -> {new_value}""")
	return text


def generate_error_message(error: str, err_message, message: types.Message) -> str:
	first_name = message.from_user.first_name
	last_name: str | None = message.from_user.last_name
	username = message.from_user.username
	user_id = message.from_user.id
	text = message.text
	return (f'{error}: {err_message}\n'
			f'First name: {first_name}\n'
			f'Last name: {last_name}\n'
			f'Username: {username}\n'
			f'User id: {user_id}\n'
			f'User text: {text}')
