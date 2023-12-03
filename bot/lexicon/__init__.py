from services.defs import create_courses

# file with bot text


# bot lexicon
lexicon_ru = {
    'hello': 'Привет, я бот для проверки тестов, на спиженных курсах',
    'courses': 'Выбери нужный курс',
    'choose_part': 'Выбери часть',
    'choose_lesson': 'Выбери урок',
    'choose_page': 'Выбери страницу',
    'test_not_founded': 'В этом модуле тест не найден 😔',
    'all_tests': 'Больше нет тестов'

}
LEXICON = {
    'forward': '>>',
    'backward': '<<',
}
courses = create_courses()
