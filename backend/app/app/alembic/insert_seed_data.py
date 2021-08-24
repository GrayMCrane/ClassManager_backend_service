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
    insert_family_relation_config(op)
    insert_subjects(op)
    op.execute("select setval('class_id_seq', 1001, false);")


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


# 插入 亲属关系 的配置
def insert_family_relation_config(op):
    family_relation_config = [
        {
            'key': '1',
            'value': '本人',
            'desc': '亲属关系: 本人',
            'type': DBConst.FAMILY_RELATION,
        },
        {
            'key': '2',
            'value': '爸爸',
            'desc': '亲属关系: 爸爸',
            'type': DBConst.FAMILY_RELATION,
        },
        {
            'key': '3',
            'value': '妈妈',
            'desc': '亲属关系: 妈妈',
            'type': DBConst.FAMILY_RELATION,
        },
        {
            'key': '4',
            'value': '爷爷',
            'desc': '亲属关系: 爷爷',
            'type': DBConst.FAMILY_RELATION,
        },
        {
            'key': '5',
            'value': '奶奶',
            'desc': '亲属关系: 奶奶',
            'type': DBConst.FAMILY_RELATION,
        },
        {
            'key': '6',
            'value': '外公',
            'desc': '亲属关系: 外公',
            'type': DBConst.FAMILY_RELATION,
        },
        {
            'key': '7',
            'value': '外婆',
            'desc': '亲属关系: 外婆',
            'type': DBConst.FAMILY_RELATION,
        },
        {
            'key': '8',
            'value': '哥哥',
            'desc': '亲属关系: 哥哥',
            'type': DBConst.FAMILY_RELATION,
        },
        {
            'key': '9',
            'value': '姐姐',
            'desc': '亲属关系: 姐姐',
            'type': DBConst.FAMILY_RELATION,
        },
    ]
    op.bulk_insert(sys_config_table, family_relation_config)


# 插入 学科 预置数据
def insert_subjects(op):
    subject_table = table(
        'subject',
        column('name')
    )
    subjects = [{'name': '语文'}, {'name': '数学'}, {'name': '英语'}]
    op.bulk_insert(subject_table, subjects)


entrance_page_table = table(
    'entrance_page',
    column('src'), column('target'), column('type')
)


# 插入 启动页及引导页 图片
def insert_entrance_pages(op):
    startup_pages = [
        {'src': '/files/pics/startup_v1.svg', 'target': None, 'type': '1'}
    ]
    op.bulk_insert(entrance_page_table, startup_pages)
