from taskiq_redis import ListQueueBroker

from src.config import get_config

config = get_config()

broker = ListQueueBroker(
    config.taskiq.url,
    queue="posts",
)


@broker.task
async def send_post(post_id: int):
    pass
