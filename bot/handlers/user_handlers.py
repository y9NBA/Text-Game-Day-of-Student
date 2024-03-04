from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import Message, KeyboardButton, MenuButton, MenuButtonCommands, BotCommand, CallbackQuery
from bot.keyboards.user_kb import *
from DataBase.db import *
from bot.states.user_states import *

import re


async def cmd_start(msg: Message, state: FSMContext) -> None:
    reply_text = f"Приветствуем вас, {msg.from_user.first_name}."
    await msg.bot.set_chat_menu_button(msg.from_user.id, None)
    await msg.bot.set_my_commands(commands=[
        BotCommand("main_menu", "Главное меню"),
        BotCommand("login", "Настройка логина")
    ])
    await msg.answer(text=reply_text)
    await start_menu(msg, state)


async def start_menu(call: CallbackQuery | Message, state: FSMContext):
    await state.finish()
    reply_text = title_text("Главное меню")
    # exist = await DB.user_exists(call.from_user.id)
    exist = bool(User.get_or_none(usertgID=call.from_user.id) is None)
    if exist:
        reply_text += "\n"
        reply_text += "Нажмите на кнопку \"Логин\" и введите свой логин для игры."
    await call.bot.send_message(call.from_user.id, text=reply_text, reply_markup=get_start_kb())


async def login(call: CallbackQuery | Message, state: FSMContext) -> None:
    # exist = await DB.user_exists(call.from_user.id)
    exist = bool(User.get_or_none(usertgID=call.from_user.id) is None)
    if not exist:
        # user_login = await DB.get_userlogin(call.from_user.id)
        user = User.get(usertgID=call.from_user.id)
        reply_text = f"Ваш Логин: {user.login}" + "\nДля изменения просто введите новый Логин."
    else:
        reply_text = ("Введите свой логин для игры")
    await call.bot.send_message(call.from_user.id, text=reply_text, reply_markup=get_login_kb())
    await state.set_state(States.waiting_enter_login)


def title_text(string: str) -> str:
    string = "#" * len(string) + "\n" + string + "\n" + "#" * len(string)
    return string


async def enter_login(msg: Message, state: FSMContext) -> None:
    if re.match("^[a-zA-Z](.[a-zA-Z0-9_-]*)$", msg.text):
        # exist = await DB.user_exists(msg.from_user.id)
        exist = bool(User.get_or_none(usertgID=msg.from_user.id) is None)
        if not exist:
            # await DB.update_userlogin(msg.from_user.id, msg.text)
            user = User.get(usertgID=msg.from_user.id)
            user.login = msg.text
            user.save()
        else:
            # await DB.add_user
            User.create(login=msg.text, usertgID=msg.from_user.id, role=2)
        await msg.answer("Логин успешно установлен")
    else:
        await msg.answer("Некорректный Логин\nВаш логин должен содержать буквы латинского алфавита, также он может содержать цифры и " +
                     "символы нижнего подчёркивания.")
    await state.finish()
    await login(msg, state)


async def unknown(msg: Message):
    await msg.answer("Неизвестная команда!")


def reg_handler(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_start, CommandStart(), state="*")
    dp.register_message_handler(start_menu, commands=["main_menu"], state="*")
    dp.register_message_handler(login, commands=["login"], state="*")
    dp.register_callback_query_handler(login, Text(callbacks[0]), state="*")
    dp.register_callback_query_handler(start_menu, Text(callbacks_back[0]), state="*")
    dp.register_message_handler(enter_login, state=States.waiting_enter_login)

    dp.register_message_handler(unknown, state="*")
    