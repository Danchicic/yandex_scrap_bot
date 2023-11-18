import os

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon import courses
import json


class Keyboard:
    """
    class keyboard have builders for kb's
    """

    def __init__(self, kb):
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
