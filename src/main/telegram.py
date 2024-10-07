from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from src.config import Config
from src.presentation.aiogram.filters import ChatIDFilter
from src.presentation.aiogram.routes.main import router as main_router
from src.presentation.aiogram.routes.set_pair import router as set_pair_router


def setup_aiogram(config: Config) -> tuple[Bot, Dispatcher]:
    bot = Bot(config.telegram.token)

    storage = RedisStorage(Redis.from_url(
        url=config.redis.dsn(config.telegram.fsm_storage_database)
    ))
    dp = Dispatcher(storage=storage)

    dp.include_router(main_router)

    # dp.include_routers(main_router, set_pair_router)
    # dp.message.filter(ChatIDFilter(config.telegram.main_chat_id))
    # dp.callback_query.filter(ChatIDFilter(config.telegram.main_chat_id))

    return bot, dp
