from adaptix import Retort
from sqlalchemy import delete, select, insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.enums.send_order import SendOrderEnum
from src.application.errors import DatabaseError
from src.application.errors import NotFoundError
from src.application.schema.chat import ChatPairSchema
from src.infra.postgres.tables import BaseDBModel, ChatPairModel


class BasePostgresGateway:
    def __init__(self, retort: Retort, session: AsyncSession, table: type[BaseDBModel]) -> None:
        self.retort = retort
        self.session = session
        self.table = table

    async def delete_by_id(self, entity_id: int | str) -> int | str:
        """Удаляет сущность по id."""
        stmt = delete(self.table).where(self.table.id == entity_id)

        try:
            result = await self.session.execute(stmt)
            if result.rowcount != 1:
                raise NotFoundError(model_name='chat')

            return entity_id
        except IntegrityError as e:
            raise DatabaseError(message=str(e)) from e


class ChatsGateway(BasePostgresGateway):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(
            retort=Retort(),
            session=session,
            table=ChatPairModel
        )

    async def get_all_pairs(self) -> list[ChatPairSchema]:
        return self.retort.load(
            (await self.session.execute(select(
                ChatPairModel
            ))).mappings().fetchall(),
            list[ChatPairSchema]
        )

    async def create_pair(self, private_chat_id: str, public_chat_id: str, send_order: SendOrderEnum) -> ChatPairSchema:
        stmt = insert(
            ChatPairModel
        ).values(
            private_chat_id=private_chat_id,
            public_chat_id=public_chat_id,
            send_order=send_order
        ).returning(
            ChatPairModel
        )
        try:
            return self.retort.load((await self.session.execute(stmt)).mappings().fetchall(), ChatPairSchema)
        except IntegrityError as e:
            match e.orig.sqlstate:
                case _:
                    raise DatabaseError(
                        message=str(e.orig),
                    ) from e
