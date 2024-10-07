from typing import Tuple, Any

from aiogram import Dispatcher, Bot
from dishka import make_async_container
from dishka.integrations.aiogram import setup_dishka as setup_dishka_aiogram
from fastapi import FastAPI
from loguru import logger

from src.config import Config
from src.config import get_config
from src.infra.loguru import setup_logging
from src.main.di import DishkaProvider
from src.main.telegram import setup_aiogram


def app() -> tuple[Bot, Dispatcher]:
    """Инициализация основного приложения."""
    config: Config = get_config()
    setup_logging(config.logging)

    container = make_async_container(DishkaProvider(config=config))
    logger.info('Initializing aiogram')

    bot, dp = setup_aiogram(
        config
    )
    setup_dishka_aiogram(container, router=dp, auto_inject=True)
    logger.info('Initialized')
    return bot, dp
