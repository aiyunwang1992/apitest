#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 11:03
# @Author  : suoer
# @File    : decorators.py
# @Software: PyCharm
from functools import wraps
'''管理所有装饰器'''

def singleton(cls):
    '''单例模式'''
    obj={}
    @wraps(cls)
    def warpper(*args,**kwargs):
        if cls not in obj:
            obj[cls]=cls(*args,**kwargs)
        return obj[cls]
    return warpper



