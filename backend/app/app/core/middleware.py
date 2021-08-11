#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/8/4
# Author: gray

"""
FastAPI中间件
"""

import time
import uuid
from typing import Callable

from fastapi import Request
from fastapi.responses import StreamingResponse
from loguru import logger


async def log_requests(
    request: Request, call_next: Callable
) -> StreamingResponse:
    """
    调用路径函数时打印日志
    调用视图函数前，打印请求路径和请求参数
    调用视图函数后，打印响应码和响应耗时
    """
    request_id = uuid.uuid4().hex
    request.state.request_id = request_id
    request.state.started = time.perf_counter()
    logger.info(f'rid={request_id} {request.method} {request.url.path}')
    response = await call_next(request)
    logger.info(f'rid={request_id} '
                f'completed in {time.perf_counter() - request.state.started}s '
                f'status code {response.status_code}')
    return response
