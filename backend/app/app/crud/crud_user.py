#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/13
# @Author: gray

"""
CRUD模块 - 用户相关 非复杂业务CRUD
"""

from sqlalchemy.engine.row import Row
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
    def is_openid_exists(self, db: Session, openid: str) -> User:
        """
        判断 openid 对应的用户是否存在，存在则返回 id
        """
        return (
            db.query(self.model.id)
            .filter(User.openid == openid)
            .first()
        )

    def get_basic_info(self, db: Session, user_id: int) -> Row:
        """
        获取用户基本信息
        """
        return (
            db.query(self.model.current_member_id, self.model.is_delete)
            .filter(User.id == user_id)
            .first()
        )

    def update_current_member(self, db: Session, user_id: int, member_id: int):
        """
        更新用户当前所在班级
        """
        res = (
            db.query(self.model.id)
            .filter(User.id == user_id)
            .update({'current_member_id': member_id})
        )
        db.commit()
        return res


user = CRUDUser(User)
