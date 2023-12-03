import os

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from lexicon import courses, LEXICON
import json


class Keyboard:
    """
    class keyboard have builders for kb's
    """

    def __init__(self, kb=''):
        """
        initializing kb name and
        file with func to use
        :param kb:
        """
        self.kb: str = kb
        with open('keyboards/actions.json', 'r', encoding='utf-8') as f:
            self.actions = json.load(f)

    @staticmethod
    def create_directories_kb(path) -> ReplyKeyboardMarkup:
        """
         using if course have new directory with lessons
        :param path: local path with directories
        :return:
        """

        builder = ReplyKeyboardBuilder()
        buttons: list[KeyboardButton] = []

        for lesson in os.listdir(path):
            if os.path.isdir(path + lesson):
                buttons.append(KeyboardButton(text=lesson))

        buttons.sort(key=lambda button: button.text)

        builder.row(*buttons, width=4)
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

    @staticmethod
    def create_courses_kb() -> ReplyKeyboardMarkup:
        """
        main kb for all courses
        :return: kb as markup to handlers.
        """
        builder = ReplyKeyboardBuilder()
        buttons: list[KeyboardButton] = [KeyboardButton(text=course) for course in courses]
        builder.row(*buttons, width=4)
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

    @staticmethod
    def create_kb_from_list(buttons_names: list) -> ReplyKeyboardMarkup:
        """
        creating kb from the list of button's
        :param buttons_names: button names list
        :rtype: kb object
        """
        builder = ReplyKeyboardBuilder()
        buttons: list[KeyboardButton] = [KeyboardButton(text=button) for button in buttons_names]
        builder.row(*buttons, width=4)
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

    @staticmethod
    def create_inline_answers_kb(correct: list[bool], next_buttons: list[str]) -> InlineKeyboardMarkup:
        """
        :param next_buttons:
        :param correct: correct answers
        :return:
        """
        buttons: list[InlineKeyboardButton] = []
        kb_builder = InlineKeyboardBuilder()
        for i in range(1, len(correct) + 1):
            # print(i)
            buttons.append(
                InlineKeyboardButton(text=str(i), callback_data=str(correct[i - 1]))
            )
        if next_buttons:
            kb_builder.row(*[InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button) for button in next_buttons]
                           )
        kb_builder.row(*buttons, width=2)
        return kb_builder.as_markup()

    def get_kb(self, *args):
        """
        func to call builders in a class
        :param args: path
        :return:
        """
        # if had args(path) we need to call directory func
        if args:
            course_path = args[0]
            for row in self.actions:
                if row['text'] == self.kb:
                    return getattr(self, row['func'])(course_path)

        # actions from json file
        for row in self.actions:
            if row['text'] == self.kb:
                return getattr(self, row['func'])()


if __name__ == '__main__':
    pass
