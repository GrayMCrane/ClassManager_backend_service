#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/8/16
# Author: gray

"""
路径函数 - 配置相关
"""

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.constants import DBConst


router = APIRouter()


@router.get('/subjects', summary='查询学科配置')
def get_subjects(
    db: Session = Depends(deps.get_db),
    _: schemas.TokenPayload = Depends(deps.get_activated)
) -> Any:
    """
    查询学科配置
    """
    return crud.subject.all(db)


@router.get('/family_relations', summary='查询亲属关系配置')
def get_family_relations(
    db: Session = Depends(deps.get_db),
    _: schemas.TokenPayload = Depends(deps.get_activated)
) -> Any:
    """
    查询亲属关系配置
    """
    return crud.sys_config.get_config_by_type(db, type_=DBConst.FAMILY_RELATION)
