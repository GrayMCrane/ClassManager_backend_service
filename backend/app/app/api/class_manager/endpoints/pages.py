#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/7/28
# Author: gray

"""
路径函数 - 页面相关
"""

from typing import Any

from fastapi import APIRouter, Depends
from loguru import logger
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.constants import RespError
from app.exceptions import BizHTTPException


router = APIRouter()

SLIDESHOW_NUMBER_LIMIT = 10
HOMEPAGE_MENU_NUMBER_LIMIT = 8


@router.get('/slideshows')
def get_slideshows(
    db: Session = Depends(deps.get_db),
    limit: int = SLIDESHOW_NUMBER_LIMIT,
) -> Any:
    """
    获取启用中的轮播图，图片数量有限制
    """
    try:
        if not limit or limit <= 0 or limit > SLIDESHOW_NUMBER_LIMIT:
            limit = SLIDESHOW_NUMBER_LIMIT
        slideshows = crud.slideshow.get_activated(db, limit=limit)
        return slideshows
    except Exception:
        logger.exception(f'Failed to get slideshow')
        raise BizHTTPException(*RespError.INTERNAL_SERVER_ERROR)


@router.get('/homepage_menus')
def get_homepage_menus(
    db: Session = Depends(deps.get_db),
    _: schemas.TokenPayload = Depends(deps.get_activated),
    limit: int = HOMEPAGE_MENU_NUMBER_LIMIT,
) -> Any:
    """
    获取首页菜单，有数量限制
    """
    try:
        if not limit or limit <= 0 or limit > HOMEPAGE_MENU_NUMBER_LIMIT:
            limit = HOMEPAGE_MENU_NUMBER_LIMIT
        homepage_menus = crud.homepage_menu.get_activated(db, limit)
        return homepage_menus
    except Exception:
        logger.exception(f'Failed to get homepage menu')
        raise BizHTTPException(*RespError.INTERNAL_SERVER_ERROR)
