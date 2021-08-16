#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/7/30
# Author: gray

"""
CRUD模块 - 学校相关 非复杂业务CRUD
"""

from typing import List

from sqlalchemy.engine.row import Row
from sqlalchemy.orm import Session
from sqlalchemy.sql import and_, false, func, null

from app.crud.base import CRUDBase
from app.constants import DBConst
from app.models import Apply4Class, Class, ClassMember, Subject


class CRUDClass(CRUDBase[Class, Class, Class]):
    """
    班级相关CRUD  模型类: Class  数据表: class
    """
    def class_exists(
        self, db: Session, class_id: int
    ) -> Row[Class.id, Class.contact, Class.need_audit]:
        """
        查询 class_id 对应班级是否存在
        """
        return (
            db.query(self.model.id, self.model.contact, self.model.need_audit)
            .filter(
                and_(
                    Class.id == class_id,
                    self.model.is_delete == false()
                )
            )
            .first()
        )

    def get_class_id_by_telephone(self, db: Session, telephone: int) -> int:
        """
        根据班主任的电话号码获取班级码
        """
        return (
            db.query(self.model.id.label('class_code'))
            .filter(
                and_(
                    Class.contact == telephone,
                    Class.is_delete == false(),
                )
            )
            .first()
        )


class CRUDClassMember(CRUDBase[ClassMember, ClassMember, ClassMember]):
    """
    班级成员相关CRUD  模型类: ClassMember  数据表: class_member
    """
    def is_teacher_in_class(self, db: Session, user_id: int) -> Row:
        """
        查询老师是否在班，如已在班，返回任教学科
        """
        return (
            db.query(
                self.model.subject_id.label('id'), Subject.name.label('name')
            )
            .join(Subject, self.model.subject_id == Subject.id)
            .filter(
                and_(
                    ClassMember.user_id == user_id,
                    ClassMember.member_role.in_(
                        (DBConst.HEADTEACHER, DBConst.TEACHER)
                    ),
                    ClassMember.is_delete == false(),
                )
            )
            .first()
        )

    def is_student_in_class(self, db: Session, user_id: int, name: str) -> Row:
        """
        查询学生是否已在班
        """
        return (
            db.query(func.count(self.model.id))
            .filter(
                and_(
                    ClassMember.user_id == user_id,
                    ClassMember.name == name,
                    ClassMember.is_delete == false(),
                )
            )
            .scalar()
        )

    def get_family_members(self, db: Session, class_id: int, name: str) -> List[Row]:  # noqa
        """
        根据班级码和学生姓名查询亲属列表
        """
        return (
            db.query(self.model.name, self.model.family_relation,
                     self.model.telephone)
            .filter(
                and_(
                    ClassMember.class_id == class_id,
                    ClassMember.name == name,
                    ClassMember.member_role == DBConst.STUDENT,
                    ClassMember.is_delete == false(),
                )
            )
            .all()
        )

    def get_current_class_member(
        self, db: Session, user_id: int, member_id: int
    ) -> Row:
        """
        查询当前用户的班级成员信息
        """
        return (
            db.query(self.model.id, self.model.class_id, self.model.name,
                     self.model.member_role, self.model.subject_id,
                     self.model.family_relation, Class.class_, Class.grade)
            .join(Class, self.model.classid == Class.id)
            .filter(
                and_(
                    ClassMember.id == member_id,
                    ClassMember.user_id == user_id,
                    ClassMember.is_delete == false(),
                    Class.is_delete == false(),
                )
            )
            .first()
        )

    def get_class_members(self, db: Session, user_id: int) -> List[Row]:
        """
        根据 user_id 查询该用户的所有作为班级成员的信息
        """
        return (
            db.query(self.model.id, self.model.class_id, self.model.name,
                     self.model.member_role, self.model.family_relation,
                     Class.class_, Class.grade)
            .join(Class, self.model.class_id == Class.id)
            .filter(
                and_(
                    ClassMember.user_id == user_id,
                    ClassMember.is_delete == false(),
                    Class.is_delete == false()
                )
            )
            .all()
        )

    def subject_teacher_exists(
        self, db: Session, class_id: int, subject_id: int
    ) -> Row:
        """
        查询对应科目是否已有任课老师，如有，返回该科目名称
        """
        return (
            db.query(self.model.id, Subject.name)
            .join(Subject, self.model.subject_id == Subject.id)
            .filter(
                and_(
                    ClassMember.class_id == class_id,
                    ClassMember.subject_id == subject_id,
                    ClassMember.is_delete == false(),
                    Subject.is_delete == false(),
                )
            )
            .first()
        )


class CRUDApply4Class(CRUDBase[Apply4Class, Apply4Class, Apply4Class]):
    """
    班级成员相关CRUD  模型类: ClassMember  数据表: class_member
    """
    def teacher_apply_exists(
        self, db: Session, user_id: int, class_id: int
    ) -> int:
        """
        查询老师的入班申请是否已提交，如已提交，返回入班申请相关信息
        """
        return (
            db.query(func.count(self.model.id))
            .filter(
                and_(
                    Apply4Class.user_id == user_id,
                    Apply4Class.class_id == class_id,
                    Apply4Class.result != DBConst.REJECT,
                    Apply4Class.subject_id != null(),
                )
            )
            .scalar()
        )

    def student_apply_exists(
        self, db: Session, user_id: int, class_id: int
    ) -> List[Row[Apply4Class.name]]:
        """
        查询 同一用户在同一班级内同一学生名字提交学生入班申请的数量
        """
        return (
            db.query(self.model.name)
            .filter(
                and_(
                    Apply4Class.user_id == user_id,
                    Apply4Class.class_id == class_id,
                    Apply4Class.result != DBConst.REJECT,
                    Apply4Class.subject_id == null(),
                )
            )
            .all()
        )


class_ = CRUDClass(Class)
class_member = CRUDClassMember(ClassMember)
apply4class = CRUDApply4Class(Apply4Class)
