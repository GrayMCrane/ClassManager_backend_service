from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    openid: str


# Properties to receive via API on creation
class UserCreate(UserBase):
    ...
