#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date: 2021/8/3
# Author: gray

from sqlalchemy.orm import Session

from app import crud
from app.models import HomepageMenu, Slideshow
from app.tests.utils.utils import random_lower_string


def create_random_slideshow(db: Session) -> Slideshow:
    src = random_lower_string()
    desc = random_lower_string()
    target = random_lower_string()
    herf = random_lower_string()
    name = random_lower_string()

    slideshow = Slideshow(src=src, desc=desc, target=target, herf=herf, name=name)  # noqa
    crud.entrance_page.create(db, obj_in=slideshow)
    return slideshow


def create_random_homepage_menu(db: Session) -> HomepageMenu:
    target = random_lower_string()
    title = random_lower_string()
    icon = random_lower_string()

    homepage_menu = HomepageMenu(target=target, title=title, icon=icon)
    crud.homepage_menu.create(db, obj_in=homepage_menu)
    return homepage_menu
