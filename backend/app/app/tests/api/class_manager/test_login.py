#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/8/3
# Author: gray

def test_get_access_token(token: str) -> None:
    assert token
    assert isinstance(token, str)
