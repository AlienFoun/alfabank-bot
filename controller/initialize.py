from aiogram import Bot, Dispatcher, types

from loguru import logger
from notifiers.logging import NotificationHandler

from constants import EXPORT_CHAT_ID
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)

defaults = {'token': BOT_TOKEN, 'chat_id': EXPORT_CHAT_ID}
handler = NotificationHandler('telegram', defaults=defaults)

logger.add(handler)
