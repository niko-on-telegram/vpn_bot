from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from aiogram.types import Chat
from aiogram.types import Message


class ChatIDFilter(BaseFilter):
    def __init__(self, chat_id: int) -> None:
        self.chat_id = chat_id

    async def __call__(self, message: Message | CallbackQuery) -> bool:
        match message:
            case Message(chat=Chat(id=chat_id, username=username)):
                return chat_id == self.chat_id or username == self.chat_id
            case CallbackQuery(
                message=Message(chat=Chat(id=chat_id, username=username))
            ):
                return chat_id == self.chat_id or username == self.chat_id
