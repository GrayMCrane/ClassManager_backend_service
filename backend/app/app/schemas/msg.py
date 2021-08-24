"""
结构体模型类 - 外部接口报文 相关
"""

from pydantic import BaseModel


class Msg(BaseModel):
    msg: str


class Code2SessionMsg(BaseModel):
    session_key: str = None
    openid: str = None
    errcode: str = None
    errmsg: str = None


class WXAccessTokenMsg(BaseModel):
    access_token: str = None
    expires_in: int = None
    errcode: str = None
    errmsg: str = None
