#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/8/5
# Author: gray

"""
路径函数 - 用户相关
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps


router = APIRouter()


@router.get('/info', summary='查询用户基本信息')
def get_user_basic_info(
    db: Session = Depends(deps.get_db),
    token: schemas.TokenPayload = Depends(deps.get_activated),
):
    """
    查询用户在 当前所在班级的 信息
    """
    user_id = token.sub
    cur_member_id = token.user.current_member_id
    return crud.class_member.get_current_class_member(db, user_id, cur_member_id)
