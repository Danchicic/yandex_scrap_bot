from dataclasses import dataclass
from environs import Env


@dataclass
class UserData:
    user_id: int
    page: int


@dataclass
class LocalPaths:
    path_zero: str
    course_path: str
    part_path: str
    lesson_path: str
    test_path: str


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot
    paths: LocalPaths
    db: UserData


env = Env()
env.read_env()

config = Config(
    tg_bot=TgBot(
        token=env('BOT_TOKEN'),
    ),
    paths=LocalPaths(
        path_zero='/Users/danya/Desktop/курсы/',
        course_path='',
        part_path='',
        lesson_path='',
        test_path='',
    ),
    db=UserData(
        user_id=999999999,
        page=0,

    )
)
