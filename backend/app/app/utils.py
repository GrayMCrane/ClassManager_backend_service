#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/8/9
# Author: gray

"""
公共工具模块
"""

import os
import sys

from loguru import logger

from app.core.config import settings


def init_logger():
    """
    初始化日志系统
    日志路径为 项目根目录下的log目录
    日志等级为 .env 文件中 LOG_LEVEL 配置项
    日志分为两种，一为 runtime_YYYY-MM-DD.log 文件名的运行时日志，
        另一种为 error_YYYY-MM-DD.log 文件名的错误日志
    日志每天 00:00 进行绕街并压缩为zip格式
    日志系统异步（包括多进程和协程）安全，可以将 enqueue=True 删除以提高性能，但会丧失异步安全特性
    """
    log_dir = os.path.join(settings.BASE_DIR, 'log')
    logger.remove()
    if settings.LOG_LEVEL in ('TRACE', 'DEBUG'):
        logger.add(sink=sys.stderr, level=settings.LOG_LEVEL)
    logger.add(
        sink=os.path.join(log_dir, 'runtime_{time:YYYY-MM-DD}.log'),
        level=settings.LOG_LEVEL,
        rotation='00:00',
        enqueue=True,
        compression='zip',
    )
    logger.add(
        sink=os.path.join(log_dir, 'error_{time:YYYY-MM-DD}.log'),
        level='ERROR',
        rotation='00:00',
        enqueue=True,
        compression='zip',
    )
