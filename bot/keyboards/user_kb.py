from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from DataBase.models import dict_classes


callbacks = ["user_login", "profile", "classes"]
callbacks_back = ["main_menu"]

classes = [x for x in dict_classes]


def get_start_kb() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Логин", callback_data=callbacks[0])],
        [InlineKeyboardButton(text="Специальности", callback_data=callbacks[2])]
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
    classes_kb = [
            [
                InlineKeyboardButton(text=classes[i], callback_data=classes[i]),
                InlineKeyboardButton(text=classes[i+1], callback_data=classes[i+1])
            ]
            for i in range(0, len(classes), 2)
            if i+1 < len(classes)
    ]
    classes_kb.append([InlineKeyboardButton(text=classes[-1], callback_data=classes[-1])])
    classes_kb.append([InlineKeyboardButton(text="< Назад", callback_data=callbacks_back[0])])
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=classes_kb
    )
    return keyboard


def get_enter_class_kb(class_name: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Выбрать класс', callback_data=class_name)],
        [InlineKeyboardButton(text="< Назад", callback_data=callbacks[2])]
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
