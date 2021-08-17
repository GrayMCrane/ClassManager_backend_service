#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/8/9
# Author: gray

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models import Subject


def test_subjects(client: TestClient, token_headers: dict, db: Session) -> None:
    if not db.query(Subject).filter(Subject.name == '语文').first():
        db.add(Subject(name='语文'))
        db.commit()
    if not db.query(Subject).filter(Subject.name == '数学').first():
        db.add(Subject(name='数学'))
        db.commit()
    resp = client.get(
        f'{settings.CLASS_MANAGER_STR}/subjects', headers=token_headers
    )
    assert resp.status_code == 200
    content = resp.json()
    assert content
    assert [x for x in content if x.get('name') == '语文']
    assert [x for x in content if x.get('name') == '数学']
