import os
from bs4.element import Tag
from bs4 import BeautifulSoup

from scrapper.filters_for_soup import quiz_filter, quiz_answers_filter


def get_files(path: str):
    path = '/Users/danya/Desktop/курсы/Django/2_/01_О курсе'
    path += '/'
    files_path = []
    tasks = []
    for filename in os.listdir(path):
        if '.mht' in filename or '.html' in filename:
            files_path.append(path + filename)
        elif os.path.isdir(path + filename) and 'files' not in filename:
            # if directory in lesson directory, this directory is tasks for lessons
            if os.path.isdir(path + filename):
                tasks.append(f"{path}{filename}/{filename}.mht")
            else:
                tasks.append(f"{path}{filename}")

    print(files_path, tasks)


def delete_answers_from_file(path: str) -> dict[str, dict[tuple[str], list]]:
    """
    func take path of file delete test from file and returning test

    :param paths:
    :return: dict like {'question?': {ans1: bool(0, 1)} } where 1 is mean answer is True
    """
    tests_dict: dict[str, dict[tuple[str], list]] = {}
    # open file with test
    with open(path) as f:
        soup = BeautifulSoup(f, 'lxml')

    # find quiz's
    tests = soup.find_all(quiz_filter)
    # save page
    page = str(soup)

    # iter for answers on page
    for test in tests:
        # replace test in file, with the text
        page = page.replace(str(test), 'Решить тест в Боте!!!')

        # find question
        question = test.find('div', class_='paragraph')

        # list for dict structure
        text_answers: list[str] = []
        correct: list[bool] = []

        for ans in test.find_all(quiz_answers_filter):
            text_answers.append(ans.find('label').text)
            correct.append(isinstance(ans.find(class_='quiz-form-choice__feedback'), Tag))
        tests_dict[question.text] = {tuple(text_answers): correct}

    with open('new_html.html', 'w+') as new_file:
        new_file.writelines(page)
    print(tests_dict)
    return tests_dict


def replace_all_tests():
    with open('tests_file.txt', 'w+') as f:
        for path in paths_list:
            test = delete_answers_from_file(path)
            f.write(f"{path}::{test}\n")


def main():
    replace_all_tests()
    # delete_answers_from_file(
    #     '/Users/danya/Desktop/курсы/Django/2_/02_Введение в базы данных/01_Введение_в_базы_данных.html')


if __name__ == '__main__':
    main()
