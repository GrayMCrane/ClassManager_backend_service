#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/13
# @Author: gray

"""
CRUD模块 - 用户相关 非复杂业务CRUD
"""

from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.crud.base import CRUDBase
from app.models.user import User


class CRUDUser(CRUDBase[User, User, User]):
    """
    用户相关，非复杂业务CRUD
    模型类: User
    数据表: user
    """
    def has_openid(self, db: Session, openid: str):
        """
        查询 user 表内是否已存在对应 openid
        """
        return (
            db.query(func.count(self.model.id))
            .filter(User.openid == openid)
            .scalar()
        )


user = CRUDUser(User)
