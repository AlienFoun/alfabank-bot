from constants import TABLE_NAME
from bot_commands import COMMAND_TO_COLUMN

import pygsheets


def get_names(worksheet):
	data_from_table = worksheet.get_values('A', 'C')
	clear_data = list(filter(lambda x: x[1] != '', data_from_table))  # remove empty fields
	id_name = {}
	for element in clear_data:
		id_name[element[1]] = (element[2], element[0])
	return id_name


def update_table(user_id, message_text):
	id_names = get_names(worksheet)

	full_name, number = id_names[str(user_id)]

	column = COMMAND_TO_COLUMN[message_text]

	old_value = worksheet.cell(f'{column}{number}').value
	old_value = int(old_value) if old_value != "" else 0

	new_value = old_value + 1

	worksheet.update_value(f'{column}{number}', f'{new_value}')
	return full_name, old_value, new_value


client = pygsheets.authorize(service_account_file='../service.json')
sheet = client.open(TABLE_NAME)
worksheet = sheet.worksheet_by_title('SALES')
