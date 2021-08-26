#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/8/5
# Author: gray

"""
路径函数 - 用户相关
"""

import secrets

from fastapi import APIRouter, Depends, Body
from fastapi.responses import JSONResponse
from redis import Redis
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.constants import RespError
from app.core.celery_app import celery_app
from app.core.config import settings
from app.exceptions import BizHTTPException


router = APIRouter()

TELEPHONE_REGEX = r'^1[358]\d{9}$|^147\d{8}$|^179\d{8}$'


@router.get('/info', summary='查询用户基本信息')
def get_user_basic_info(
    db: Session = Depends(deps.get_db),
    token: schemas.TokenPayload = Depends(deps.get_activated),
):
    """
    查询用户在 当前所在班级的 信息
    """
    user_id = int(token.sub)
    cur_member_id = token.user.current_member_id
    return crud.class_member.get_current_class_member(db, user_id, cur_member_id)


@router.post('/telephone/sms_captcha/request', summary='请求手机短信验证码')
def send_sms_captcha(
    request_id: int = Depends(deps.get_request_id),
    _: schemas.TokenPayload = Depends(deps.get_activated),
    redis: Redis = Depends(deps.get_redis),
    telephone: str = Body(..., regex=TELEPHONE_REGEX, description='电话号码'),
) -> JSONResponse:
    """
    通过短信发送手机号验证码
    """
    # 从Redis获取该手机号对应的 send_flag，
    # 若 send_flag 已存在则判定为发送过于频繁，此时不予发送短信
    send_flag = redis.get(f'send_flag_{telephone}')
    if send_flag:
        raise BizHTTPException(*RespError.USER_REQUESTS_TOO_FREQUENTLY)
    # 生成随机验证码
    captcha = secrets.randbelow(999999)
    # 向celery推送短信发送任务
    celery_app.send_task(
        'worker.send_sms_captcha',
        args=[
            request_id,
            telephone,
            captcha,
            settings.SMS_CAPTCHA_EXPIRE_SECONDS // 60,
        ]
    )
    # 存储 send_flag 和 验证码 到Redis
    redis.setex(f'send_flag_{telephone}', settings.SEND_SMS_INTERVAL_SECONDS, 1)
    redis.setex(
        f'sms_captcha_{telephone}', settings.SMS_CAPTCHA_EXPIRE_SECONDS, captcha
    )
    return JSONResponse()
