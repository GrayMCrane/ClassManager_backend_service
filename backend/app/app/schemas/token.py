from typing import Any

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    iss: str
    aud: str
    sub: str
    flag: str
    sub_sign: str
    user: Any = None
