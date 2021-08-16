#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/7/28
# Author: gray

"""
路径函数 - 页面相关
"""

from typing import Any

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps


router = APIRouter()

SLIDESHOW_NUMBER_LIMIT = 10
HOMEPAGE_MENU_NUMBER_LIMIT = 8


@router.get('/slideshows', summary='获取轮播图', description='获取轮播图')
def get_slideshows(
    db: Session = Depends(deps.get_db),
    limit: int = Query(SLIDESHOW_NUMBER_LIMIT, description='数量'),
) -> Any:
    """
    获取启用中的轮播图，图片数量有限制
    """
    if not limit or limit <= 0 or limit > SLIDESHOW_NUMBER_LIMIT:
        limit = SLIDESHOW_NUMBER_LIMIT
    slideshows = crud.slideshow.get_activated(db, limit=limit)
    return slideshows


@router.get('/homepage_menus', summary='获取首页菜单', description='获取首页菜单')
def get_homepage_menus(
    db: Session = Depends(deps.get_db),
    _: schemas.TokenPayload = Depends(deps.get_activated),
    limit: int = Query(HOMEPAGE_MENU_NUMBER_LIMIT, description='数量'),
) -> Any:
    """
    获取首页菜单，有数量限制
    """
    if not limit or limit <= 0 or limit > HOMEPAGE_MENU_NUMBER_LIMIT:
        limit = HOMEPAGE_MENU_NUMBER_LIMIT
    homepage_menus = crud.homepage_menu.get_activated(db, limit)
    return homepage_menus
