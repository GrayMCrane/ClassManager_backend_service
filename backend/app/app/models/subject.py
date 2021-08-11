#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/8
# @Author: gray

"""
ORM模型类 - 学科
"""

from sqlalchemy.schema import Column
from sqlalchemy.sql import text
from sqlalchemy.types import Boolean, Integer, String

from app.models.base import Base


class Subject(Base):
    """
    学科
    数据表: subject - 描述学科的基本信息
    """
    id = Column(
        Integer, primary_key=True, autoincrement=True, comment='学科id，主键'
    )
    name = Column(String(20), nullable=True, unique=True, comment='学科名')
    is_delete = Column(
        Boolean, server_default=text('False'), nullable=False, comment='是否删除'
    )
    
    __no_update_time__ = True
