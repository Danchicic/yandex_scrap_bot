from bs4 import Tag


def quiz_filter(tag: Tag):
    # print(tag.attrs)
    return 'quiz' in tag.attrs['class'] if tag.has_attr('class') else 0


def quiz_answers_filter(tag: Tag):
    return 'quiz-form-choice__option' in tag.attrs['class'] if tag.has_attr('class') else 0
