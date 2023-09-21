from typing import List, Dict, Tuple


def generate_dict_from_table(data_from_table: List[str]) -> Dict[str, Tuple[str, str]]:
	clear_data = list(filter(lambda lst: lst[1] != '', data_from_table))  # remove empty fields
	id_name = {}
	for element in clear_data:
		id_name[element[1]] = (element[2], element[0])
	return id_name
