#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/8
# @Author: gray

"""
ORM模型类 - 班级相关
"""

from sqlalchemy.schema import Column
from sqlalchemy.types import BigInteger, Boolean, Integer, String, TIMESTAMP

from app.db.base_class import Base


class Class(Base):
    """
    班级
    数据表: class - 描述班级的基本信息
    """
    id = Column(
        BigInteger, primary_key=True, autoincrement=True, comment='班级id，主键'
    )
    school_id = Column(BigInteger, nullable=False, comment='所属学校id')
    grade = Column(Integer, comment='年级')
    _class = Column('class', Integer, comment='班级')
    need_audit = Column(Boolean, default=True, nullable=False, comment='加入班级是否需要审核')  # noqa
    created_time = Column(TIMESTAMP, nullable=False, comment='创建时间')
    updated_time = Column(TIMESTAMP, comment='最后修改时间')
    is_delete = Column(Boolean, default=False, nullable=False, comment='是否删除')

    __idx_list__ = ('school_id', )


class ClassMember(Base):
    """
    班级成员
    数据表: class_member - 描述班级成员的信息
    """
    __tablename__ = 'class_member'  # noqa

    id = Column(BigInteger, primary_key=True, autoincrement=True,
                comment='id，主键')
    class_id = Column(BigInteger, nullable=False, comment='班级id')
    user_id = Column(BigInteger, comment='用户id')
    name = Column(String, nullable=False, comment='教师/学生姓名')
    member_role = Column(String(3), nullable=False,
                         comment='成员身份: 1-班主任 2-任课老师 3-学生 4-学生亲属')
    subject = Column(Integer, comment='任教科目id')
    family_relation = Column(String(3), comment='亲属关系id: '
                                                '1-本人 2-爸爸 3-妈妈 4-爷爷 5-奶奶 '
                                                '6-外公 7-外婆 8-哥哥 9-姐姐')
    telephone = Column(String(11), nullable=False, comment='电话号码')
    create_time = Column(TIMESTAMP, nullable=False, comment='创建时间')
    update_time = Column(TIMESTAMP, comment='最后修改时间')
    is_delete = Column(Boolean, default=False, nullable=False, comment='是否删除')

    __idx_list__ = ('class_id', 'user_id', 'name')


class Apply4Class(Base):
    """
    入班申请
    数据表: apply4class - 入班申请信息
    """
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='主键')
    proposer = Column(BigInteger, nullable=False, comment='申请人姓名')
    proposer_id = Column(BigInteger, nullable=False, comment='申请人id')
    auditor = Column(BigInteger, comment='审核人姓名')
    auditor_user_id = Column(BigInteger, comment='审核人的班级成员id')
    class_id = Column(BigInteger, nullable=False, comment='申请加入班级的id')  # noqa
    subject_id = Column(Integer, comment='任教科目id')
    telephone = Column(String(11), comment='电话号码')
    result = Column(
        String(2), nullable=False, default=1, comment='审核结果: 0-驳回 1-待审核 2-通过'
    )
    start_time = Column(TIMESTAMP, nullable=False, comment='发起时间')
    end_time = Column(TIMESTAMP, comment='结束时间')

    __idx_list__ = ('proposer_id', 'class_id')


class Group(Base):
    """
    班级小组
    """
