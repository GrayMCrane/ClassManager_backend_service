#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/8
# @Author: gray

"""
ORM模型类 - 作业相关
"""

from sqlalchemy.schema import Column
from sqlalchemy.types import BigInteger, Boolean, String, Text, TIMESTAMP

from app.models.base import Base


class Homework(Base):
    """
    作业
    数据表: homework - 发布的作业的信息
    """
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='id，主键')  # noqa
    pub_time = Column(TIMESTAMP, nullable=False, comment='发布时间')
    end_time = Column(TIMESTAMP, nullable=False, comment='截止时间')
    publisher = Column(BigInteger, nullable=False, comment='发布人')
    class_id = Column(BigInteger, nullable=False, comment='发布班级')
    title = Column(String, nullable=False, comment='作业标题')
    desc = Column(Text, nullable=False, comment='作业描述')
    stu_reviewable = Column(Boolean, nullable=False, comment='同学间是否可互相查看')

    __idx_list__ = ('class_id', 'title')
