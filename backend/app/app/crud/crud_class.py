#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/7/30
# Author: gray

"""
CRUD模块 - 学校相关 非复杂业务CRUD
"""

from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql import and_, false

from app.crud.base import CRUDBase
from app.constants import DBConst
from app.models import Class, ClassMember


class CRUDClass(CRUDBase[Class, Class, Class]):
    """
    班级相关CRUD
    模型类: Class
    数据表: class
    """
    def get_class_id_by_telephone(self, db: Session, telephone: int) -> int:
        """
        根据班主任的电话号码获取班级码
        """
        return (
            db.query(self.model.id.label('class_code'))
            .join(ClassMember, self.model.id == ClassMember.class_id)
            .filter(
                and_(
                    ClassMember.is_delete == false(),
                    Class.is_delete == false(),
                    ClassMember.member_role == DBConst.HEADTEACHER,
                    ClassMember.telephone == telephone,
                )
            )
            .first()
        )


class CRUDClassMember(CRUDBase[ClassMember, ClassMember, ClassMember]):
    """
    班级成员相关CRUD
    模型类: ClassMember
    数据表: class_member
    """
    def get_family_members(
        self, db: Session, class_id: int, name: str
    ) -> List[ClassMember]:
        """
        根据班级码和学生姓名查询亲属列表
        """
        return (
            db.query(self.model.name, self.model.family_relation,
                     self.model.telephone)
            .filter(
                and_(
                    ClassMember.is_delete == false(),
                    ClassMember.class_id == class_id,
                    ClassMember.name == name,
                    ClassMember.member_role == DBConst.STUDENT,
                )
            )
            .all()
        )


class_ = CRUDClass(Class)
class_member = CRUDClassMember(ClassMember)
