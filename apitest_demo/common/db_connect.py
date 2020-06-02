# !/usr/bin/python
# -*- encoding: utf-8 -*-
# 用于连接数据库的类
import mysql.connector
from common.config import Config
from common.loger import Log

from common.Singleton_decorator import Sdecorator
from conf.projectpath import *

log = Log()


@Sdecorator
class DBCONN():
    def __init__(self):

        self.db_config = Config().configer(db_path, 'DB', 'db_conf')

    # 建立数据库连接，获取游标
    def db_conn(self):
        # 建立数据库连接并登陆
        conn = mysql.connector.connect(**self.db_config)
        return conn

    # 建立游标
    def __enter__(self, conn):
        cursor = conn.cursor()
        return cursor

    # 进行数据操库作
    def db_operation(self, sql, type=1):
        # 建立游标
        conn = self.db_conn()
        cursor = conn.cursor()
        # 输入sql语句并执行
        cursor.execute(sql)
        # 加入异常的判断
        try:
            if type == 1:
                # 返回一条查询结果
                sql_result = cursor.fetchone()
            else:
                # 返回所有查询结果
                sql_result = cursor.fetchall()
            return sql_result
        except Exception as e:
            log.error('查询报错：{0}'.format(e))

    def __exit__(self, cursor, conn, exc_type, exc_val, exc_tb):
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()
    # 关闭游标，关闭数据库连接
    # def close_db(self,conn,cursor):
    # cursor.close()
    # conn.close()


if __name__ == '__main__':
    sql = "SELECT * from f_user where fid=1"
    sql_result = list(iter(DBCONN().db_operation(sql, 2)))
    for i in sql_result:
        param = {'id': i}
        print(param)
