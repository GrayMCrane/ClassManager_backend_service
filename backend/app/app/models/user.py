#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/7
# @Author: gray

"""
ORM模型类 - 用户
"""

from sqlalchemy.schema import Column
from sqlalchemy.sql import text
from sqlalchemy.types import BigInteger, Boolean, String

from app.models.base import Base


class User(Base):
    """
    用户
    数据表: user - 描述用户的基础信息
    """
    id = Column(
        BigInteger, primary_key=True, autoincrement=True, comment='用户id，主键'
    )
    wx_name = Column(String, comment='微信名称')
    avatar = Column(String, comment='头像URL')
    openid = Column(String, nullable=False, unique=True, comment='用户openid')
    telephone = Column(String(11), comment='电话号码')
    current_member_id = Column(BigInteger, comment='当前班级成员id')
    is_delete = Column(
        Boolean, server_default=text('False'), nullable=False, comment='是否删除'
    )

    __idx_list__ = ('openid', 'wx_name')
