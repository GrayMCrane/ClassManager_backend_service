#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/8/5
# Author: gray

"""
异常处理 - 宽泛的异常
"""

import traceback

from fastapi import Request
from fastapi.responses import JSONResponse
from loguru import logger

from app.schemas import Response
from app.constants import RespError


async def broad_exception_handler(
    request: Request, __: Exception
) -> JSONResponse:
    """
    统一处理意料之外的异常
    返回异常响应并记录错误栈日志
    """
    logger.error(f'rid={request.state.request_id} '
                 f'headers={request.headers} body={await request.body()} '
                 f'an unexpected exception occurred:\n{traceback.format_exc()}')
    return Response(*RespError.INTERNAL_SERVER_ERROR)
