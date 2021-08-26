#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/7/27
# Author: gray

"""
异常响应 相关
"""

from fastapi import Request
from fastapi.responses import JSONResponse
from loguru import logger

from app.schemas import Response
from app.exceptions import BizHTTPException


async def http_exception_handler(
    request: Request, exc: BizHTTPException
) -> JSONResponse:
    """
    统一处理 HTTPException 异常
    返回异常响应并记录错误栈日志
    """
    logger.error(f'rid={request.state.request_id} '
                 f'an http exception occurred: {exc}')
    data = getattr(exc, 'data', None)
    headers = getattr(exc, "headers", None)
    return Response(exc.status_code, exc.statement, exc.message, data, headers)
