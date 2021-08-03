#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/7
# @Author: gray

"""
ORM模型类 - 学校
"""

from sqlalchemy.schema import Column
from sqlalchemy.types import BigInteger, Boolean, Integer, String

from app.models.base import Base


class School(Base):
    """
    学校
    数据表: school - 描述学校信息
    """
    id = Column(
        BigInteger, primary_key=True, autoincrement=True, comment='学校id，主键'
    )
    name = Column(String, nullable=False, comment='学校名称')
    region_code = Column(Integer, nullable=False, comment='所在地区的地区码')
    address = Column(String, comment='学校地址')
    study_stage = Column(String, comment='学段，多个值以","分隔: 1-小学 2-初中 3-高中')
    school_id = Column(BigInteger, unique=True, comment='云平台 - 学校id')
    parent_org_id = Column(BigInteger, comment='云平台 - 上级机构id')
    curr_cpscode = Column(Integer, comment='全品学码')  # noqa
    data_source = Column(
        String(2), nullable=False, comment='数据来源: 1-api网关同步 2-小学数字教辅中心创建'
    )
    is_delete = Column(Boolean, default=False, nullable=False, comment='是否删除')
