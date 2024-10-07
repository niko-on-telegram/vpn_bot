from datetime import datetime
from typing import Any

from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.application.enums.chat_type import ChatTypeEnum
from src.application.enums.post_status import PostStatusEnum
from src.application.enums.send_order import SendOrderEnum
from src.infra.postgres.utils import integer_id


class BaseDBModel(DeclarativeBase):
    __tablename__: Any
    __table_args__: dict[str, str] | tuple = {'schema': 'sender_schema'}


class PostModel(BaseDBModel):
    __tablename__ = "posts"
    __table_args__ = {'schema': 'sender_schema'}

    id: Mapped[integer_id]
    message_id: Mapped[int] = mapped_column(nullable=False)
    chat_id: Mapped[int] = mapped_column(ForeignKey(
        'sender_schema.chat_pairs.id'
    ), nullable=False)

    status: Mapped[PostStatusEnum] = mapped_column(default=PostStatusEnum.NOT_SENT, nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)


class ChatPairModel(BaseDBModel):
    __tablename__ = 'chat_pairs'
    __table_args__ = {'schema': 'sender_schema'}

    id: Mapped[integer_id]
    public_chat_id: Mapped[str] = mapped_column(nullable=False)
    private_chat_id: Mapped[str] = mapped_column(nullable=False)
    send_order: Mapped[SendOrderEnum] = mapped_column(nullable=False)
