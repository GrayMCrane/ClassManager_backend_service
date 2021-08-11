#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/8/4
# Author: gray

"""
CRUD模块 - 学科相关 非复杂业务CRUD
"""

from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql import false

from app.crud.base import CRUDBase
from app.models import Subject


class CRUDSubject(CRUDBase[Subject, Subject, Subject]):
    """
    学科相关CRUD
    模型类: Subject
    数据表: subject
    """
    def all(self, db: Session) -> List[Subject]:
        """
        获取所有学科数据
        """
        return (
            db.query(self.model.id.label('code'), self.model.name)
            .filter(Subject.is_delete == false())
            .all()
        )


subject = CRUDSubject(Subject)
