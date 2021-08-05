#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/8/5
# Author: gray

"""
异常处理 - 宽泛的异常
"""

from fastapi import Request
from fastapi.responses import JSONResponse
from loguru import logger

from app.constants import RespError


async def broad_exception_handler(_: Request, __: Exception) -> JSONResponse:
    """
    统一处理意料之外的异常
    返回异常响应并记录错误栈日志
    """
    logger.exception('An unexpected exception occurred')
    status_code, detail, desc = RespError.INTERNAL_SERVER_ERROR
    return JSONResponse({'detail': detail, 'desc': desc},
                        status_code=status_code)
