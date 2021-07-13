#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/12
# @Author: gray

"""
ORM模型类 - 页面相关
"""

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from app.db.base_class import Base


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
    status = Column(String(2), nullable=False, comment='状态')
    # TODO: 激活状态，版本，是否删除？


class Slideshow(Base):
    """
    轮播图
    数据表: slideshow - 首次进入小程序的轮播图的信息
    """
    id = Column(Integer, primary_key=True, autoincrement=True, comment='id，主键')
    src = Column(String, nullable=False, comment='图片链接')
    desc = Column(String, comment='图片描述')
    target = Column(String, comment='页面路由')
    herf = Column(String, comment='跳转外链')
    name = Column(String, comment='名字')
    status = Column(String(2), nullable=False, comment='状态')
    # TODO: 激活状态，版本，是否删除？
