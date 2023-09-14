def generate_answer(full_name: str, message_text: str, old_value: int, new_value: int):
	surname, name, *second_name = full_name.split()
	text = (f"""Фамилия: {surname}\n"""
			f"""Имя: {name}\n"""
			f"""Отчество: {" ".join(second_name)}\n"""
			f"""Сообщение: {message_text}\n"""
			f"""Изменения в таблице: {old_value} -> {new_value}""")
	return text