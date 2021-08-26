#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/12
# @Author: gray

"""
ORM模型类 - 用户反馈
"""

from sqlalchemy.schema import Column
from sqlalchemy.types import BigInteger, Integer, Text

from app.models.base import Base


class Feedback(Base):
    """
    用户反馈
    数据表: feedback - 用户反馈的信息
    """
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='主键')
    user_id = Column(BigInteger, nullable=False, comment='用户id')
    category = Column(Integer, nullable=False, comment='反馈类型')
    desc = Column(Text, nullable=False, comment='反馈内容描述')

    __idx_list__ = ('user_id', )
    __no_update_time__ = True


class FeedbackImage(Base):
    """
    用户反馈图片
    数据表: feedback_image - 用户反馈的图片
    """
    __tablename__ = 'feedback_image'  # noqa

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='主键')
    feedback_id = Column(BigInteger, nullable=False, comment='用户反馈id')
    order = Column(Integer, nullable=False, comment='顺序')
    base64 = Column(Text, nullable=False, comment='图片base64数据')

    __idx_list__ = ('feedback_id', )
    __no_update_time__ = True
