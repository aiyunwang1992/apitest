#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 11:10
# @Author  : suoer
# @File    : projectpath.py
# @Software: PyCharm
'''项目各文件路径'''
import os
#项目路径
basepath=os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
#http.conf
httpconf_path=os.path.join(basepath,'conf','http.conf')
#register
register_path=os.path.join(basepath,'testdatas','register.yaml')
#login
login_path=os.path.join(basepath,'testdatas','login.yaml')
#用例
testcases_path=os.path.join(basepath,'testcases')
#测试报告
reports_path=os.path.join(basepath,'testreports','reports')
#日志
logs_path=os.path.join(basepath,'testreports','logs')
#email
email_path=os.path.join(basepath,'conf','email.conf')
#数据库信息
db_path=os.path.join(basepath,'conf','db.conf')
#身份认证
identify_path=os.path.join(basepath,'testdatas','junior_identity.yaml')
#注册成功的手机号
reginphone_path=os.path.join(basepath,'conf','reginphone.yaml')