from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from DataBase.models import dict_classes


callbacks = ["user_login", "profile", "view_classes"]
callbacks_back = ["user_login_b", "profile_b", "view_classes_b"]


def get_start_kb() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Логин", callback_data=callbacks[0])
    ]
    ])
    return keyboard


def get_login_kb() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="< Назад", callback_data=callbacks_back[0])
    ]
    ])
    return keyboard


def get_view_classes_kb() -> InlineKeyboardMarkup:
    classes_kb = [InlineKeyboardButton(text=f"{x}") for x in dict_classes.keys()]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        classes_kb.append(InlineKeyboardButton(text="< Назад", callback_data=callbacks_back[2]))
    ])
    return keyboard


'''def get_profile() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Логин", callback_data=callbacks[1]),
            InlineKeyboardButton(text="< Назад", callback_data=callbacks_back[1])
        ]
    ])
    return keyboard'''
