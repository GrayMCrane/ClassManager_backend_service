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

    # -------------- 轮播图表 slideshow 相关 -------------
    SLIDESHOW_ACTIVATED = '1'    # 轮播图已启用
    SLIDESHOW_INACTIVATED = '0'  # 轮播图已停用

    # ------------ 首页菜单 homepage_menu 相关 -----------
    HOMEPAGE_MENU_ACTIVATED = '1'    # 首页菜单项已启用
    HOMEPAGE_MENU_INACTIVATED = '0'  # 首页菜单项已停用

    # ----------- 班级成员表 class_member 相关 -----------
    HEADTEACHER = '1'  # 班级成员身份: 班主任
    TEACHER = '2'      # 班级成员身份: 任课老师
    STUDENT = '3'      # 班级成员身份: 学生
