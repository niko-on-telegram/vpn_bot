from dataclasses import dataclass

from adaptix import Retort

from src.application.enums.send_order import SendOrderEnum

retort = Retort()


@dataclass(slots=True)
class CreateChatPairSchema:
    private_chat_id: str
    public_chat_id: str
    send_order: SendOrderEnum
