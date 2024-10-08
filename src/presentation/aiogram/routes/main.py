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
        Pre("""vmess://eyJhZGQiOiAiMzUuMjI2LjI1MC4zIiwgImFpZCI6ICIwIiwgImhvc3QiOiAiZ29vZ2xlLmNvbSIsICJpZCI6ICIyZWRjZDRjZS02OWQ3LTQ0M2ItYTVhMi1mZGU0MDAxOTUxMTIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwODEsICJwcyI6ICJcdWQ4M2RcdWRlODAgTWFyeiAodGVzdF91c2VyKSBbVk1lc3MgLSB0Y3BdIiwgInNjeSI6ICJhdXRvIiwgInRscyI6ICJub25lIiwgInR5cGUiOiAiaHR0cCIsICJ2IjogIjIifQ==

vmess://eyJhZGQiOiAiMzUuMjI2LjI1MC4zIiwgImFpZCI6ICIwIiwgImhvc3QiOiAiZ29vZ2xlLmNvbSIsICJpZCI6ICIyZWRjZDRjZS02OWQ3LTQ0M2ItYTVhMi1mZGU0MDAxOTUxMTIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogODA4MCwgInBzIjogIlx1ZDgzZFx1ZGU4MCBNYXJ6ICh0ZXN0X3VzZXIpIFtWTWVzcyAtIHdzXSIsICJzY3kiOiAiYXV0byIsICJ0bHMiOiAibm9uZSIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==

vless://96588cfa-9303-4128-b7fb-c3e1796f8401@35.226.250.3:8443?security=reality&type=tcp&headerType=&path=&host=&sni=cdn.discordapp.com&fp=chrome&pbk=SbVKOEMjK0sIlbwg4akyBg5mL5KZwwB-ed4eEE7YnRc&sid=#%F0%9F%9A%80%20Marz%20%28test_user%29%20%5BVLESS%20-%20tcp%5D

vless://96588cfa-9303-4128-b7fb-c3e1796f8401@35.226.250.3:2053?security=reality&type=grpc&headerType=&serviceName=xyz&authority=&mode=gun&sni=cdn.discordapp.com&fp=chrome&pbk=SbVKOEMjK0sIlbwg4akyBg5mL5KZwwB-ed4eEE7YnRc&sid=#%F0%9F%9A%80%20Marz%20%28test_user%29%20%5BVLESS%20-%20grpc%5D

trojan://-fB-CPiadsRksx5GpAQiGw@35.226.250.3:2083?security=tls&type=ws&headerType=&path=&host=&sni=8ec8d36e04160a75.metric.gstatic.com&fp=#%F0%9F%9A%80%20Marz%20%28test_user%29%20%5BTrojan%20-%20ws%5D

ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpqdGxBLU5oX05VRGZkNkVtNzRWMC13@35.226.250.3:1080#%F0%9F%9A%80%20Marz%20%28test_user%29%20%5BShadowsocks%20-%20tcp%5D

False"""),
    )

    await message.answer(**text.as_kwargs())

# @router.message(Command('chats'))
# async def set_settings(message: Message, chats_gateway: FromDishka[ChatsGateway]) -> None:
#     await message.answer(
#         "\n".join(
#             [format_chat_pair_schema(pair) for pair in await chats_gateway.get_all_pairs()]
#         )
#     )
