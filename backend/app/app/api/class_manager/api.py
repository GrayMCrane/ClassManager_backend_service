from fastapi import APIRouter

from app.api.class_manager.endpoints import login, pages, classes


api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(pages.router, prefix='/pages', tags=['pages'])
api_router.include_router(classes.router, prefix='/classes', tags=['classes'])
