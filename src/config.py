import logging
import os

from dataclasses import dataclass
from dataclasses import field

from adaptix import Retort
from dynaconf import Dynaconf


@dataclass(slots=True)
class ApiConfig:
    host: str
    port: int

    debug: bool = False

    project_name: str = 'template'
    project_path: str = field(
        default_factory=lambda: os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..')
        )
    )


@dataclass(slots=True)
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str
    database: str
    driver: str = 'postgresql+asyncpg'

    @property
    def dsn(self) -> str:
        """Сборка dsn для базы данных."""
        return f'{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'


@dataclass(slots=True)
class LoggingConfig:
    level: str
    human_readable_logs: bool = True


@dataclass(slots=True)
class RedisConfig:
    host: str
    port: int
    username: str | None = None
    password: str | None = None
    database: str = '0'
    driver: str = 'redis'

    def dsn(self, database: str | None = None) -> str:
        """Сборка dsn для базы данных."""
        if self.username is None and self.password is None:
            return f'{self.driver}://{self.host}:{self.port}/{self.database}'
        return f'{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{database or self.database}'


@dataclass(slots=True)
class TelegramConfig:
    token: str
    main_chat_id: int
    fsm_storage_database: str = '1'


@dataclass(slots=True)
class Config:
    api: ApiConfig
    redis: RedisConfig
    telegram: TelegramConfig
    database: DatabaseConfig
    logging: LoggingConfig


def get_config() -> Config:
    """Парсинг dotenv и получение конфига."""
    config_path = os.path.abspath(os.getenv('CONFIG_PATH'))
    assert os.path.exists(config_path)
    logging.info(f"{config_path=}")
    dynaconf = Dynaconf(
        settings_files=[config_path],
        # envvar_prefix='RESENDER',
        # load_dotenv=True,
    )
    retort = Retort()

    return retort.load(dynaconf, Config)
