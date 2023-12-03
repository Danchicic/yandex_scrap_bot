import os


# file to additional func

def create_courses():
    courses = []
    path_zero = '/Users/danya/Desktop/курсы'
    for filename in os.listdir(path_zero):
        if '.' not in filename:
            courses.append(filename)
    return courses


def read_tests() -> dict[str, dict]:
    headers, tests = [], []
    with open('../scrapper/tests_file.txt') as file:
        for row in file:
            head, test = row.split('::')
            headers.append(head)
            # change the type from str to dic
            tests.append(eval(test))

    return dict(zip(headers, tests))


def dict_indexing(db: dict, index=0) -> tuple:
    index += 1
    index_value = tuple(db.values())[index]
    index_key = tuple(db.keys())[index]
    return index_key, index_value


def create_text_for_bot(func):
    """decorator"""

    def wrapper(*args):
        question, answers, correct = func(*args)
        string = f"{question}\n\n"
        string += '\n\n'.join(answers)
        if sum(correct) > 1:
            string += '\n\n<i>В этом тесте больше одного ответа</i>'
        return string, correct

    return wrapper
