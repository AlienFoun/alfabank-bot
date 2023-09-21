from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from constants import IMPORT_CHAT_ID
from bot_commands import COMMAND_FILTER

from controller.funcs import main, check_id


def register_all_handlers(dp: Dispatcher):
	dp.register_message_handler(main, Text(equals=COMMAND_FILTER), chat_id=IMPORT_CHAT_ID)
	dp.register_message_handler(check_id, commands=['check'])
