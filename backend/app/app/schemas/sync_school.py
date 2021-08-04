#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/16
# @Author: gray

"""
结构体模型类 - 同步学校数据接口的响应数据结构
"""

from typing import List

from pydantic import BaseModel


class SyncSchool(BaseModel):
    schoolId: int
    schoolName: str
    parentOrgId: int = None
    periodName: str
    currCpscode: int = None
    cityName: str
    areaName: str
    address: str = None
    status: int
    telephone: str = None


class SchoolData(BaseModel):
    totalPage: int
    list: List[SyncSchool]


class SyncSchoolRespContent(BaseModel):
    data: SchoolData
