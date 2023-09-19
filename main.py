from aiogram import executor
from controller.funcs import start_bot_message, shutdown_bot_message
from controller.register import register_all_handlers
from controller.initialize import dp

register_all_handlers(dp)

if __name__ == '__main__':
	executor.start_polling(dp, on_startup=start_bot_message, on_shutdown=shutdown_bot_message)
	#executor.start_polling(dp)
