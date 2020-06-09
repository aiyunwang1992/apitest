#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 12:22
# @Author  : suoer
# @File    : replace_value.py
# @Software: PyCharm
#正则表达式提取器
from common.save_value import SaveValue
class ReplaceValue():
    '''进行参数替换'''
    def __init__(self,data):
        self.data=data
    def replace_param(self,value,new_value):
        if new_value and value in self.data['param']:
            self.data['param']=self.data['param'].replace(value,new_value)
        else:
            pass
        return self.data
if __name__ == '__main__':
    b = [{ 'param':"{'ticket':'TICKET'}", 'code':123456}]
    reg = ReplaceValue(b)
    value='TICKET'
    print(reg.replace_param(value,SaveValue.TICKET))