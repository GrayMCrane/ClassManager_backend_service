#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/14
# @Author: gray

"""
初始化数据库时插入种子数据
"""

import os

from sqlalchemy.sql import table, column

from app.constants import DBConst


def insert_seed_data(op) -> None:
    insert_region(op)
    insert_cp_field_mapping(op)


# 插入 地区 种子数据
def insert_region(op) -> None:
    region_table = table(
        'region',
        column('code'),
        column('name'),
        column('code'),
        column('parent_code'),
        column('level')
    )

    region_seed = []
    csv = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'region.csv')
    with open(csv) as f:
        for seq in f:
            code, name, parent_code, level = seq.split(',')
            parent_code = parent_code if parent_code else None
            level = level.strip()
            region_seed.append(
                {
                    'code': code,
                    'name': name,
                    'parent_code': parent_code,
                    'level': level,
                }
            )
        region_seed.pop(0) if region_seed else ...

    op.bulk_insert(
        region_table,
        region_seed
    )


sys_config_table = table(
    'sys_config',
    column('key'),
    column('value'),
    column('desc'),
    column('type')
)


# 插入从 API网关接口 同步数据时的字段映射配置
def insert_cp_field_mapping(op):
    # API网关 学段 与我数据库 学段 字段的常量值映射
    school_phase_mapping = [
        {
            'key': '1',
            'value': '小学',
            'desc': '学段: 小学',
            'type': DBConst.SCHOOL_STUDY_STAGE,
        },
        {
            'key': '2',
            'value': '初中',
            'desc': '学段: 初中',
            'type': DBConst.SCHOOL_STUDY_STAGE,
        },
        {
            'key': '3',
            'value': '高中',
            'desc': '学段: 高中',
            'type': DBConst.SCHOOL_STUDY_STAGE,
        },
    ]
    op.bulk_insert(sys_config_table, school_phase_mapping)
