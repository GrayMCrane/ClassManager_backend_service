#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/13
# @Author: gray

"""
CRUD模块 - 用户相关 非复杂业务CRUD
"""

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import User
from app.schemas.user import UserCreate


class CRUDUser(CRUDBase[User, UserCreate, User]):
    """
    用户相关，非复杂业务CRUD
    模型类: User
    数据表: user
    """
    def get_user_by_openid(self, db: Session, openid: str) -> User:
        return (
            db.query(self.model)
            .filter(User.openid == openid)
            .first()
        )


user = CRUDUser(User)
