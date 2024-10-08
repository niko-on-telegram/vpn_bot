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
            'vless://96588cfa-9303-4128-b7fb-c3e1796f8401@35.226.250.3:8443?security=reality&type=tcp&headerType'
            '=&path=&host=&sni=discordapp.com&fp=chrome&pbk=SbVKOEMjK0sIlbwg4akyBg5mL5KZwwB-ed4eEE7YnRc&sid=#%F0%9F'
            '%9A%80%20Marz%20%28test_user%29%20%5BVLESS%20-%20tcp%5D'
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
