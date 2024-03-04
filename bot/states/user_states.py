from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class States(StatesGroup):

    # main_menu = State("main_menu")
    # view_classes = State("view_classes")
    waiting_enter_login = State("waiting_enter_login")
    waiting_enter_class = State("waiting_enter_class")
