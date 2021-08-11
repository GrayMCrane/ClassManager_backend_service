#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/7/27
# Author: gray

"""
异常响应 相关
"""

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from loguru import logger

from app.exceptions import BizHTTPException


async def http_exception_handler(
    request: Request, exc: HTTPException
) -> JSONResponse:
    """
    统一处理 HTTPException 异常
    返回异常响应并记录错误栈日志
    """
    if isinstance(exc, BizHTTPException):
        logger.error(f'rid={request.state.request_id} '
                     f'an http exception occurred: {exc}')
    else:
        logger.exception(
            f'rid={request.state.request_id} '
            f'headers={request.headers} body={await request.body()} '
            f'an http exception occurred:'
        )
    headers = getattr(exc, "headers", None)
    desc = getattr(exc, 'desc', None)
    content = {'detail': exc.detail}
    if desc:
        content['desc'] = desc
    if headers:
        return JSONResponse(
            content, status_code=exc.status_code,
            headers=headers
        )
    else:
        return JSONResponse(content, status_code=exc.status_code)
