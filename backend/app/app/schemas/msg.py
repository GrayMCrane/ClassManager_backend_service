from pydantic import BaseModel


class Msg(BaseModel):
    msg: str


class Code2SessionMsg(BaseModel):
    session_key: str = None
    openid: str = None
    errcode: str = None
    errmsg: str = None
