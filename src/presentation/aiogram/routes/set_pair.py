from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from dishka import FromDishka
from loguru import logger

from src.application.enums.send_order import SendOrderEnum
from src.application.schema.chat import ChatPairSchema
from src.infra.postgres.gateways import ChatsGateway
from src.presentation.aiogram.keyboards import submit_keyboard, post_order_keyboard
from src.presentation.aiogram.schema import retort, CreateChatPairSchema

router = Router()


class SetPairSG(StatesGroup):
    PUBLIC = State()
    PRIVATE = State()
    ORDER = State()
    SUBMIT = State()


@router.message(Command('new_pair'))
async def create_new_pair(message: Message, state: FSMContext) -> None:
    await message.answer("Enter public chat id or username")
    await state.set_state(SetPairSG.PUBLIC)
    await state.set_data({})


@router.message(
    StateFilter(SetPairSG.PUBLIC)
)
async def set_public_chat(message: Message, state: FSMContext) -> None:
    await state.update_data(
        public_chat_id=message.text
    )
    await state.set_state(SetPairSG.PRIVATE)

    await message.answer('Enter private chat id or username')


@router.message(
    StateFilter(SetPairSG.PRIVATE)
)
async def set_private_chat(
        message: Message, state: FSMContext
) -> None:
    await state.update_data(
        private_chat_id=message.text
    )
    await state.set_state(SetPairSG.ORDER)
    await message.answer('Enter post send order',
                         reply_markup=post_order_keyboard())


@router.callback_query(
    StateFilter(SetPairSG.ORDER),
    F.callback_data.in_(SendOrderEnum.values())
)
async def set_send_order(
        query: CallbackQuery, state: FSMContext
) -> None:
    logger.info("Set send order")
    await state.update_data(
        send_order=query.text
    )
    await state.set_state(SetPairSG.SUBMIT)

    data = (await state.get_data())

    public_chat_id = data['public_chat_id']
    private_chat_id = data['private_chat_id']
    send_order = data['send_order']
    await query.answer(
        'Are you sure? [yes, no]\n'
        'New chat pair:\n'
        f'Private Chat: {private_chat_id}\n'
        f'Public Chat: {public_chat_id}'
        f'Send Order: {send_order}',
        reply_markup=submit_keyboard()
    )


@router.callback_query(
    StateFilter(SetPairSG.SUBMIT),
    F.callback_data == 'no'
)
async def cancel_submit(
        query: CallbackQuery, state: FSMContext
):
    await state.clear()
    await (query.answer('Cancelled!'))


@router.callback_query(
    StateFilter(SetPairSG.SUBMIT),
    F.callback_data == 'yes'
)
async def submit(
        query: CallbackQuery, state: FSMContext, chats_gateway: FromDishka[ChatsGateway]
) -> None:
    logger.info()
    data = retort.load(await state.get_data(), CreateChatPairSchema)
    await chats_gateway.create_pair(
        private_chat_id=data.private_chat_id,
        public_chat_id=data.public_chat_id,
        send_order=data.send_order
    )

    await query.answer('Chat pair created!')
