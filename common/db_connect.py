#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 17:16
# @Author  : suoer
# @File    : db_connect.py
# @Software: PyCharm
from mysql import connector
from common.read_config import Config
from common.loger import Log
from common.decorators import singleton
from conf.projectpath import *
@singleton
class Dbconnect():
    '''连接数据库操作'''
    def __init__(self):
        self.log=Log()
        self.config=Config().config(db_path,'DB','db_conf')
        self.db=connector.connect(**self.config)
    #建立游标
    def db_cursor(self):
        cursor=self.db.cursor()
        return cursor
    def db(self,sql,type):
        """
        操作数据库
        :param sql: sql语句
        :param type: 参数为1时查询所有，为其他时只查询一条
        :return: 返回查询结果
        """
        cursor=self.db_cursor()
        cursor.execute(sql)
        try:
            if type==1:
                db_result=cursor.fetchall()
            else:
                db_result=cursor.fetchone()
            return db_result
        except Exception as e:
            self.log.error(f'查询报错{e}')
        finally:
            cursor.close()
            self.db.close()