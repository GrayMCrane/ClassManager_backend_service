from typing import Generator

from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud, schemas
from app.constants import RespError
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal
from app.exceptions import BizHTTPException

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.CLASS_MANAGER_STR}/access_tokens"
)


def get_request_id(request: Request) -> str:
    """
    从请求中获取 request_id
    """
    return request.state.request_id


def get_db() -> Generator:
    """
    获取数据库连接，支持协程异步
    """
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close() if db else ...


def get_token(
    db: Session = Depends(get_db), token_str: str = Depends(reusable_oauth2)
) -> schemas.TokenPayload:
    """
    校验Token，校验Token用户存在数据库中，返回Token payload
    """
    try:
        payload = jwt.decode(
            token_str, settings.SECRET_KEY,
            algorithms=[security.ALGORITHM], audience='ClassManager'
        )
        token = schemas.TokenPayload(**payload)
    except jwt.ExpiredSignatureError:
        raise BizHTTPException(*RespError.TOKEN_EXPIRED)
    except (jwt.JWTError, ValidationError):
        raise BizHTTPException(*RespError.INVALID_TOKEN)
    user = crud.user.get(db, id_=token.sub)
    if not user:
        raise BizHTTPException(*RespError.USER_NOT_FOUND)
    token.user = user
    return token


def get_activated(
    token: schemas.TokenPayload = Depends(get_token)
) -> schemas.TokenPayload:
    """
    校验Token用户是否停用，返回Token payload
    """
    if token.user.is_delete:
        raise BizHTTPException(*RespError.USER_DISABLED)
    return token
