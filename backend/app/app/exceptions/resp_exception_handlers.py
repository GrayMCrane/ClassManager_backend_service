#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/7/27
# Author: gray

"""
异常响应 相关
"""

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


async def http_exception_handler(_: Request,
                                 exc: HTTPException) -> JSONResponse:
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
