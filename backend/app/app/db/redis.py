#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/8/18
# Author: gray

from redis import ConnectionPool, Redis

from app.core.config import settings


redis_conn_pool = ConnectionPool(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True
)
redis = Redis(connection_pool=redis_conn_pool)
