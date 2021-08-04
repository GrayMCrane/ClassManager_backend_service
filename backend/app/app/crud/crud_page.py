#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/7/29
# Author: gray

"""
CRUD模块 - 页面相关 非复杂业务CRUD
"""

from typing import List

from app.constants import DBConst
from app.crud.base import CRUDBase
from app.models import HomepageMenu, Slideshow

from sqlalchemy.orm import Session


class CRUDHomepageMenu(CRUDBase[HomepageMenu, HomepageMenu, HomepageMenu]):
    """
    首页菜单相关CRUD
    模型类: HomepageMenu
    数据表: homepage_menu
    """
    def get_activated(self, db: Session, limit: int = 8) -> List:
        """
        查询当前已启用的首页菜单
        """
        return (
            db.query(self.model.id, self.model.target,
                     self.model.title, self.model.icon)
            .filter(HomepageMenu.status == DBConst.HOMEPAGE_MENU_ACTIVATED)
            .order_by(HomepageMenu.id.desc())
            .limit(limit)
            .all()
        )


class CRUDSlideshow(CRUDBase[Slideshow, Slideshow, Slideshow]):
    """
    轮播图相关CRUD
    模型类: Slideshow
    数据表: slideshow
    """
    def get_activated(self, db: Session, limit: int = 10) -> List[Slideshow]:
        """
        查询当前已启用的轮播图
        """
        return (
            db.query(
                self.model.id, self.model.src, self.model.desc,
                self.model.target, self.model.herf, self.model.name
            )
            .filter(Slideshow.status == DBConst.SLIDESHOW_ACTIVATED)
            .order_by(Slideshow.id.desc())
            .limit(limit)
            .all()
        )


homepage_menu = CRUDHomepageMenu(HomepageMenu)
slideshow = CRUDSlideshow(Slideshow)
