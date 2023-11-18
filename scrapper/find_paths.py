import os


def get_themes(course_path, part_path: str) -> dict:
    """
    get themes from ex.:django/routes/themes
    :param course_path:
    :param part_path:
    :return:
    """
    theme_and_index = dict()
    for theme in os.listdir(f"{course_path}/{part_path}"):
        if '.' not in theme:
            if theme[:2].isdigit():
                theme_and_index[int(theme[:2])] = theme
            else:
                pass
    # print('dict theme and index', theme_and_index)
    return theme_and_index


def get_tasks(new_path_zero, theme_file) -> list:
    """
    get tasks from lesson of part
    like django/1/routes/task1.mht
    or
    django/1/routes/task1/task1.mht

    :param new_path_zero:
    :param theme_file:
    :return:
    """
    tasks_path = []
    for files in os.listdir(f"{new_path_zero}/{theme_file}"):
        if 'task' in files.lower():
            if 'mht' not in files:
                tasks_path.append(f'{new_path_zero}/{theme_file}/{files}/{files}.mht')
            else:
                tasks_path.append(f'{new_path_zero}/{theme_file}/{files}')

            # print('new task', files)
        elif os.path.isdir(f'{new_path_zero}/{theme_file}/{files}'):
            pass
    # print('tasks_path', tasks_path)
    return tasks_path


def get_theme_files_and_tasks(theme_and_index: dict, course_path, part_path) -> tuple[list, list]:
    """
    get files from ex.: django/1/routes
    :param theme_and_index:
    :param course_path:
    :param part_path:
    :return:
    """
    quiz_files = []
    tasks = []
    for index, filename in theme_and_index.items():
        # print('main_dir:', filename)
        new_path_zero = f"{course_path}/{part_path}/{filename}"
        # print(new_path_zero)
        for theme_file in os.listdir(new_path_zero):
            if '.html' in theme_file:
                quiz_files.append(f"{new_path_zero}/{theme_file}")
                # print(theme_file)

            # finding a directory +
            elif 'files' not in theme_file and '.mht' not in theme_file and '.DS' not in theme_file and '.pdf' not in theme_file and '.zip' not in theme_file:
                # print('+ tasks', theme_file)
                tasks += get_tasks(new_path_zero, theme_file)
    # print('quiz_files and tasks', quiz_files, tasks, sep='\n')
    return quiz_files, tasks

    # print('new directory?', files)

    #     print('_________')
    # print()


def get_parts_path(course_path) -> tuple[list, list]:
    """
    func to get parts of courses
    like django/1, django/2

    :param course_path:
    :return:
    """
    quiz, task = [], []
    for part_path in os.listdir(course_path):
        if '.' not in part_path:
            theme_and_index = get_themes(course_path, part_path)
            quiz_t, task_t = get_theme_files_and_tasks(theme_and_index, course_path, part_path)
            quiz += quiz_t
            task += task_t
            # print(theme, theme_index)
    # print('quiz task', quiz, task, sep='\n')
    return quiz, task


def get_main_paths():
    """
    get courses path
    :return:
    """
    path_zero = '/Users/danya/Desktop/курсы'
    main_path = []
    for filename in os.listdir(path_zero):
        if '.' not in filename:
            main_path.append(f"{path_zero}/{filename}")

    # main_path = ['/Users/danya/Desktop/курсы/Django', '/Users/danya/Desktop/курсы/middle']

    tasks_path = []
    quiz_files = []
    for course_path in main_path:
        t1, t2 = get_parts_path(course_path)
        quiz_files += t1
        tasks_path += t2
    # print('main_func', tasks_path, quiz_files)
    return tasks_path, quiz_files


def main():
    """
    get paths of files and tasks
    :return:
    """
    tasks, quiz, = get_main_paths()
    print(tasks, quiz, sep='\n')


if __name__ == '__main__':
    main()
