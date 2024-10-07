from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import KeyboardBuilder, InlineKeyboardBuilder

from src.application.enums.send_order import SendOrderEnum


def submit_keyboard(

) -> InlineKeyboardMarkup:
    return InlineKeyboardBuilder(
        markup=[
            [InlineKeyboardButton(
                text="yes", callback_data='yes'
            ), InlineKeyboardButton(text="no", callback_data='no')]
        ],
    ).as_markup()


def post_order_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardBuilder(
        markup=[
            [
                InlineKeyboardButton(
                    text=SendOrderEnum.OLDEST.value,
                    callback_data=SendOrderEnum.OLDEST.value
                ),
                InlineKeyboardButton(
                    text=SendOrderEnum.RANDOM.value,
                    callback_data=SendOrderEnum.RANDOM.value
                )
            ]
        ]
    ).as_markup()
