#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/12
# @Author: gray

"""
ORM模型类 - 页面相关
"""

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from app.models.base import Base


class HomepageMenu(Base):
    """
    首页菜单
    数据表: homepage_menu - 首页菜单的信息
    """
    __tablename__ = 'homepage_menu'  # noqa

    id = Column(Integer, primary_key=True, autoincrement=True, comment='id，主键')
    target = Column(String, nullable=False, comment='资源路径')
    title = Column(String, nullable=False, comment='标题')
    icon = Column(String, nullable=False, comment='图标URL')
    status = Column(String(2), nullable=False, server_default='1',
                    comment='状态: 0-停用 1-启用')


class EntrancePage(Base):
    """
    启动页图片
    数据表: entrance_page - 首次进入小程序的启动页图片的信息
    """
    __tablename__ = 'entrance_page'  # noqa

    id = Column(Integer, primary_key=True, autoincrement=True, comment='id，主键')
    src = Column(String, nullable=False, comment='图片链接')
    desc = Column(String, comment='图片描述')
    target = Column(String, comment='页面路由')
    type = Column(String(2), nullable=False, comment='图片类型: '
                                                     '1-启动页图片 2-引导页图片')
    status = Column(String(2), nullable=False, server_default='1',
                    comment='状态: 0-停用 1-启用')
