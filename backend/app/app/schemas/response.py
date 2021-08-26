#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/8/13
# Author: gray

from typing import Any

from fastapi.responses import JSONResponse


class MakeResponse(object):
    def __call__(
        self, status_code: int = 200, statement: str = '成功',
        message: str = 'OK', data: Any = None, headers: Any = None,
    ) -> JSONResponse:
        content = {'statement': statement, 'message': message}
        if data:
            content['data'] = data
        return JSONResponse(content, status_code=status_code, headers=headers)


Response = MakeResponse()
