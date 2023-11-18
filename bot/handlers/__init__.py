from aiogram import Router

from .courses_handlers import course_router
from .lessons_handler import lesson_router
from .main_handlers import command_router
from .parts_handler import parts_router

# union routers
router_main: Router = Router()
router_main.include_router(command_router)
router_main.include_router(course_router)
router_main.include_router(parts_router)
router_main.include_router(lesson_router)
