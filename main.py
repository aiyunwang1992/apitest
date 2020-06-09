#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 15:39
# @Author  : suoer
# @File    : main.py
# @Software: PyCharm
'''测试用例执行文件'''
import pytest
import os
import time
from conf.projectpath import *
now=time.strftime('%Y-%m-%d_%H-%M-%S')
htmlreport='--html='+reports_path+'/apireport'+now+'.html'
allure_path=reports_path+'/allure-relults/'
allureFile_path='--alluredir='+allure_path
allure_report=reports_path+'/allure_report'
#pytest.main(['-m','flyback',htmlreport,testcases_path+'/test_register.py'])

pytest.main(['-v','-s','-m','flyback','--reruns','2','--reruns-delay','0.5',htmlreport,allureFile_path,testcases_path,'--disable-warnings'])
#os.system("allure generate "+allure_path+" -o "+allure_report+' --clean')

