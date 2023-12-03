Python 3.9.6
...
i have free programming courses and i want to learning it.
parser takes file.html, pop the test to scrapper/tests_file.txt
aiogram bot asking user to create path(on my computer) of course
bot send tests using inline keyboards and user can solve it

FSM:
    Finite State Machine - aiogram feature, which help the bot to understand where is user located

handlers:
    handlers for bot to catch messages
    main_handlers:
        start handler to choose the course
    courses_handlers:
        create the path to course
    parts_handler:
        create the path to part of course
    lessons_handler:
        create path to lesson of part
    quiz_handler:
        send test to user
    test_handler:
        callback handlers to solve the test
    __init__ union all handlers

keyboards:
    main_keyboards:
        include class Keyboard which create keyboards for bot
    main_menu:
        file to create menu of bot
    actions.json:
        file with names of funcs which help the Keyboard class

lexicon: lexicon for bot

services.defs: help funcs for project

bot: enter point to project (all imports written from this enter point)
config: config of bot
    UserData and Paths: hardcode database (in real project don't use this code)
<br>
scrapper:
    filters_for_soup: handwritten filters for html doc to find needed block
    find_paths: poop💩code to find all course files on local machine
    work_with_html: file that delete test from html file, using filters

