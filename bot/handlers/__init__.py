from aiogram import Router

from .courses_handlers import course_router
from .main_handlers import hello_router

router_main: Router = Router()
router_main.include_router(hello_router)
router_main.include_router(course_router)
