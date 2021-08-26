#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/8/3
# Author: gray

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.pages import (
    create_random_slideshow,
    create_random_homepage_menu,
)


def test_homepage_menus(
        client: TestClient, token_headers: dict, db: Session
) -> None:
    homepage_menu = create_random_homepage_menu(db)
    resp = client.get(
        f'{settings.CLASS_MANAGER_STR}/pages/homepage_menus',
        headers=token_headers,
    )
    assert resp.status_code == 200
    content = resp.json()
    assert content
    recent = content[0]
    assert recent['target'] == homepage_menu.target
    assert recent['title'] == homepage_menu.title
    assert recent['icon'] == homepage_menu.icon


def test_slideshows(client: TestClient, db: Session) -> None:
    slideshow = create_random_slideshow(db)
    resp = client.get(f'{settings.CLASS_MANAGER_STR}/pages/slideshows')

    assert resp.status_code == 200
    content = resp.json()
    assert content
    recent = content[0]
    assert recent['src'] == slideshow.src
    assert recent['desc'] == slideshow.desc
    assert recent['target'] == slideshow.target
    assert recent['herf'] == slideshow.herf
    assert recent['name'] == slideshow.name
