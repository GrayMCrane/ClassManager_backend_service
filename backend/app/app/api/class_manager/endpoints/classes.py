#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/7/29
# Author: gray

"""
路径函数 - 班级相关
"""

import re
from typing import Any

from fastapi import APIRouter, Depends, Form, Path, Query
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.constants import RespError
from app.exceptions import BizHTTPException


router = APIRouter()

telephone_pat = re.compile(r'^1[358]\d{9}$|^147\d{8}$|^179\d{8}$')


@router.get('/class_codes/')
def get_class_id_by_telephone(
    db: Session = Depends(deps.get_db),
    _: schemas.TokenPayload = Depends(deps.get_activated),
    telephone: str = Query(...),
) -> Any:
    """
    根据班主任的电话号码获取其班级的班级码
    """
    if not re.match(telephone_pat, telephone):
        raise BizHTTPException(*RespError.INVALID_PARAMETER)
    return crud.class_.get_class_id_by_telephone(db, telephone)


@router.get('/{class_id}/family_members/')
def get_family_members(
    db: Session = Depends(deps.get_db),
    _: schemas.TokenPayload = Depends(deps.get_activated),
    class_id: int = Path(...),
    name: str = Query(...),
) -> Any:
    """
    根据班级码及学生姓名获取该学生在该班级的亲属的信息
    """
    return crud.class_member.get_family_members(db, class_id, name)
