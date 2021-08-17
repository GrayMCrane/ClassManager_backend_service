from fastapi import APIRouter

from app.api.class_manager.endpoints import (
    classes, configurations, login, pages, users
)


api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(pages.router, prefix='/pages', tags=['pages'])
api_router.include_router(
    configurations.router, prefix='/configurations', tags=['configurations']
)
api_router.include_router(classes.router, prefix='/classes', tags=['classes'])
api_router.include_router(users.router, prefix='/users', tags=['users'])
