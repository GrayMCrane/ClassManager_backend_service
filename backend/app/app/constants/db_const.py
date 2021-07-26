#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/15
# @Author: gray

from app.constants.base import Const


class DBConst(Const):
    """
    数据库相关常量或枚举值
    """

    # ------------ 系统配置表 sys_config 相关 ------------
    SCHOOL_STUDY_STAGE = '1'  # 配置类型为该值的配置项，为 学校学段 配置

    # -------------- 学校信息表 school 相关 --------------
    SYNC_FROM_API = '1'  # 标识学校数据来源于 API网关同步

    # -------------- 全国地区表 region 相关 --------------
    PROVINCE = '1'  # 省级行政区
    CITY = '2'      # 地级行政区
    AREA = '3'      # 县级行政区
