# !/usr/bin/python
# -*- encoding: utf-8 -*-
# 在项目中要用到的文件路径
import os

# 项目包基本路径
base_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 项目ip配置路径
http_path = os.path.join(base_path, 'conf', 'http.conf')
# 测试数据的路径
test_data_path = os.path.join(base_path, 'test_data', 'test_data.yaml')
# 测试用例读取配置路径
case_path = os.path.join(base_path, 'conf', 'case.conf')
# 测试报告的路径
test_report = os.path.join(base_path, 'test_report')
# 数据库配置文件路径
db_path = os.path.join(base_path, 'conf', 'db_config.conf')
# 邮件配置文件的路径
email_path = os.path.join(base_path, 'conf', 'email.conf')
# 日志存放的路径
log_path = os.path.join(base_path, 'logs')
# 测试用例路径
testcases_path = os.path.join(base_path, 'testcases')
