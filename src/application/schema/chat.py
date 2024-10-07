from dataclasses import dataclass

from src.application.enums.send_order import SendOrderEnum


@dataclass(slots=True)
class ChatPairSchema:
    id: int
    public_chat_id: str
    private_chat_id: str
    send_order: SendOrderEnum

