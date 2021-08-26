#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/20
# @Author: gray

"""
CRUD模块 - 学校相关 非复杂业务CRUD
"""

from app.crud.base import CRUDBase
from app.models import School


class CRUDSchool(CRUDBase[School, School, School]):
    """
    全国地区配置相关CRUD
    模型类: School
    数据表: school
    """
    ...


school = CRUDSchool(School)
