#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/8/3
# Author: gray


from sqlalchemy.orm import Session

from app.core.internal import APIGateway


def test_sync_school_data(db: Session) -> None:
    APIGateway.sync_school_data(db)
