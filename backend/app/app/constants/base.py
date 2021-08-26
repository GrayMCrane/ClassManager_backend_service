#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 2021/7/15
# @Author: gray


class __Meta(type):
    class ConstError(Exception):
        ...

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError(f"Const class doesn't support rebind const ({name})")
        self.__dict__[name] = value


class Const(metaclass=__Meta):
    """
    常量基类
    继承该类的类都是常量类，为常量类的类变量赋值，则该类变量为常量
    常量类不支持实例化，不支持类变量重新赋值
    """
    def __new__(cls, *args, **kwargs):
        raise cls.ConstError("Const class doesn't support instantiate")
