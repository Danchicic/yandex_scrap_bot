import os


def create_courses():
    courses = []
    path_zero = '/Users/danya/Desktop/курсы'
    main_path = []
    for filename in os.listdir(path_zero):
        if '.' not in filename:
            courses.append(filename)
    return courses
