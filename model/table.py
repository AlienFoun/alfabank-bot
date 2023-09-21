from constants import TABLE_NAME
from bot_commands import COMMAND_TO_COLUMN
from model.helper import generate_dict_from_table

import pygsheets

from typing import Dict, Tuple


def get_names_from_google_table(worksheet: pygsheets.Worksheet) -> Dict[str, Tuple[str, str]]:
	data_from_table = worksheet.get_values('A', 'C')
	id_name = generate_dict_from_table(data_from_table)
	return id_name


def update_table(user_id: int, message_text: str) -> Tuple[str, int, int]:
	id_names = get_names_from_google_table(worksheet)
	full_name, number = id_names[str(user_id)]

	column = COMMAND_TO_COLUMN[message_text]

	old_value = worksheet.cell(f'{column}{number}').value
	old_value = int(old_value) if old_value != "" else 0

	new_value = old_value + 1

	worksheet.update_value(f'{column}{number}', f'{new_value}')
	return full_name, old_value, new_value


client = pygsheets.authorize(service_account_file='model/service.json')
sheet = client.open(TABLE_NAME)
worksheet: pygsheets.Worksheet = sheet.worksheet_by_title('SALES')
