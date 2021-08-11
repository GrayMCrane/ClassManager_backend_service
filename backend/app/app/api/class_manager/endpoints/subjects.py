#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/8/4
# Author: gray

"""
路径函数 - 学科相关
"""

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get('')
def get_subjects(
    db: Session = Depends(deps.get_db),
    _: schemas.TokenPayload = Depends(deps.get_activated)
) -> Any:
    """
    查询所有学科信息
    """
    return crud.subject.all(db)
