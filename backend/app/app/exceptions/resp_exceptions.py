#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/7/28
# Author: gray

"""
异常类 - 业务异常
"""

from typing import Any


class BizHTTPException(Exception):
    def __init__(
        self, status_code: int,  statement: Any = None,
        message: str = None, data: Any = None, headers: dict = None
    ):
        self.status_code = status_code
        self.statement = statement
        self.message = message
        self.data = data
        self.headers = headers
