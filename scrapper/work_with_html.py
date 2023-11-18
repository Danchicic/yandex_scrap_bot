import os

from bs4 import BeautifulSoup


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


def delete_answers(paths: list):
    for path in paths:
        with open(path) as f:
            soup = BeautifulSoup(f, 'lxml')
            tests = soup.find_all(class_='quiz quiz_options-type_checkbox quiz quiz_answered quiz_type_select')
            print(tests)


def main():
    delete_answers(
        ['/Users/danya/Desktop/курсы/Django/2_/02_Введение%20в%20базы%20данных/01_Введение_в_базы_данных.html'])


if __name__ == '__main__':
    main()
