#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/7/28
# Author: gray

"""
异常类 - 业务异常
"""

from typing import Any

from fastapi.exceptions import HTTPException


class BizHTTPException(HTTPException):
    def __init__(
        self, status_code: int, detail: Any = None,
        desc: str = None, headers: dict = None
    ):
        super().__init__(status_code=status_code, detail=detail, headers=headers)
        self.desc = desc
