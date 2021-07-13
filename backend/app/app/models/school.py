#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/7
# @Author: gray

"""
ORM模型类 - 学校
"""

from sqlalchemy.schema import Column
from sqlalchemy.types import BigInteger, Boolean, Integer, String, TIMESTAMP

from app.db.base_class import Base


class School(Base):
    """
    学校
    数据表: school - 描述学校信息
    """
    id = Column(
        BigInteger, primary_key=True, autoincrement=True, comment='学校id，主键'
    )
    name = Column(String, nullable=False, comment='学校名称')
    region = Column(Integer, nullable=False, comment='所在地区id')
    address = Column(String, comment='学校地址')
    school = Column(BigInteger, comment='云平台 - 学校id')
    parent_org = Column(BigInteger, comment='云平台 - 上级机构id')
    curr_cpscode = Column(Integer, comment='全品学码')
    created_time = Column(TIMESTAMP, nullable=False, comment='创建时间')
    updated_time = Column(TIMESTAMP, comment='最后修改时间')
    is_delete = Column(Boolean, default=False, nullable=False, comment='是否删除')
