#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/7/29
# Author: gray

"""
路径函数 - 登录验证相关
"""

import json
from datetime import timedelta
from typing import Dict

import requests
from fastapi import APIRouter, Depends, Path
from fastapi.exceptions import HTTPException
from loguru import logger
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.constants import RespError
from app.core import security
from app.core.config import settings
from app.exceptions import BizHTTPException
from app.schemas import Code2SessionMsg


router = APIRouter()


CODE2SESSION_ERROR_MAP = {
    '-1': RespError.SERVER_TOO_BUSY,
    '40029': RespError.INVALID_CODE,
    '45011': RespError.USER_REQUESTS_TOO_FREQUENTLY,
    '40226': RespError.HIGH_RISK_USER,
}


@router.get('/access_tokens/{code}', response_model=schemas.Token)
def get_access_token(
    db: Session = Depends(deps.get_db),
    code: str = Path(...),
) -> Dict[str, str]:
    """
    签发Token
    接受code，提交code到微信 auth.code2Session 接口，获取用户 openid、session_key 等信息
    若数据库 user 表无用户数据则新建用户数据
    用户的 id、openid、session_key 将被写入Token，其中 openid 和 session_key 写入前会进行加密
    """
    logger.info(f'Generating access-token with code {code}')
    params = {
        'appid': settings.MINI_PROGRAM_APP_ID,
        'secret': settings.MINI_PROGRAM_APP_SECRET,
        'js_code': code,
        'grant_type': 'authorization_code',
    }
    try:
        # 请求微信 auth.code2session 接口
        resp = requests.get(settings.CODE2SESSION_URL, params=params)
        resp_msg = Code2SessionMsg(**json.loads(resp.text))
        if not resp_msg.openid or not resp_msg.session_key:
            logger.error(f'Failed to obtain user openid and session_key by '
                         f'code2session API,code: {code},API message: {resp.text}')
            error = CODE2SESSION_ERROR_MAP.get(resp_msg.errcode,
                                               RespError.AUTHENTICATE_FAILED)
            raise BizHTTPException(*error)

        # 查询该openid的用户是否已在数据库内，若无则新建用户数据
        user = crud.user.get_user_by_openid(db, resp_msg.openid)
        if not user:
            new_user = schemas.UserCreate(openid=resp_msg.openid)
            user = crud.user.create(db, obj_in=new_user)

        # Token过期时间
        access_token_expires = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        # 加密openid
        flag = security.AESCrypto.encrypt(resp_msg.openid,
                                          settings.AES_KEY, settings.AES_IV)
        # 加密session_key
        sub_sign = security.AESCrypto.encrypt(resp_msg.session_key,
                                              settings.AES_KEY, settings.AES_IV)
        logger.info(f'Access-token generated with code {code}')
        return {
            'access_token': security.create_access_token(
                user.id, flag, sub_sign, access_token_expires
            ),
            'token_type': 'bearer',
        }
    except HTTPException:
        raise
    except Exception:
        logger.exception('Generate access-token failed')
        raise BizHTTPException(*RespError.INTERNAL_SERVER_ERROR)
