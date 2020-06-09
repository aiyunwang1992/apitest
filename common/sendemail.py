#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 12:17
# @Author  : suoer
# @File    : sendemail.py
# @Software: PyCharm
# !/usr/bin/python
# -*- encoding: utf-8 -*-
# 用于发送邮件，将测试报告发送到指定邮箱
# 带附件的邮件放送方式
import smtplib
import time
from common.loger import Log
from common.read_config import Config
from common.decorators import singleton
from email.mime.text import MIMEText  # 发送文字
from email.mime.multipart import MIMEMultipart  # 分多个部分发送邮件
from email.mime.application import MIMEApplication
from conf.projectpath import *

@singleton
class Sendemail():
    # 引入日志
    log = Log()
    # 发件人邮箱
    user = Config().config(email_path, 'EMAIL', 'user')
    # 邮箱密码
    pwd = Config().config(email_path, 'EMAIL', 'pwd')
    # 时间戳
    now = time.strftime('%y-%m-%d_%H_%M_%S')
    def send_email(self, email_to, filepath):
        # MIMEMultipart,分多个部分储存邮件
        msg = MIMEMultipart()
        # 邮件的主题
        msg['subject'] = self.now + '接口自动化测试报告'
        # 发件人邮箱
        msg['from'] = self.user
        # 收件人邮箱
        msg['to'] = email_to
        # 添加正文
        part = MIMEText('附件为本次接口自动化测试报告请查收！')
        msg.attach(part)
        # 添加附件
        part = MIMEApplication(open(filepath, 'rb').read())
        # 添加邮件请求头
        part.add_header('Content-Disposition', 'attachment', filename=filepath)
        msg.attach(part)
        # 连接邮箱服务器,默认端口为25
        s = smtplib.SMTP_SSL('smtp.qq.com', timeout=30)
        # 登录邮箱服务器
        s.login(self.user, self.pwd)
        # 发送邮件
        s.sendmail(self.user, email_to, msg.as_string())
        self.log.info('邮件发送成功')
        # 退出
        s.close()
if __name__ == '__main__':
    s=Sendemail()