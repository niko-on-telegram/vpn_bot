from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.formatting import Pre
from aiogram.utils.formatting import Text

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    text = Text(
        """Hello!

Your VPN link is:

""",
        Pre(
            'ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpzWnNnU2RVYTFFUkxmTzBwcEdVQ1NR@35.226.250.3:1080#%F0%9F%9A%80%20Marz%20'
            '%28123%29%20%5BShadowsocks%20-%20tcp%5D'
        ),
    )

    await message.answer(**text.as_kwargs())


# @router.message(Command('chats'))
# async def set_settings(message: Message, chats_gateway: FromDishka[ChatsGateway]) -> None:
#     await message.answer(
#         "\n".join(
#             [format_chat_pair_schema(pair) for pair in await chats_gateway.get_all_pairs()]
#         )
#     )
