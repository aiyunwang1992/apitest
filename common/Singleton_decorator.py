# !/usr/bin/python
# -*- encoding: utf-8 -*-
# 单例模式
class Sdecorator():
    __obj = None

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if not self.__obj:
            self.__obj = self.func(*args, **kwargs)
            return self.__obj
        else:
            return self.__obj
