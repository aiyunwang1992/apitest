# !/usr/bin/python
# -*- encoding: utf-8 -*-
#记录log的类
import time
import logging
from conf.projectpath import *
class Log():
    def __init__(self):
        self.log_name='autotest_log'
        self.log_path=log_path
    def get_log(self,level,msg):
        #建立日志收集器
        logger=logging.Logger(self.log_name)
        #设置日志过滤器，如果存在handlers不为空则直接打印日志，不再建立handler,避免重复打印日志
        if not logger.handlers :
            #设置默认日志级别
            logger.setLevel('DEBUG')
            #设置日志输出格式
            formater=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(lineno)s-%(name)s-日志信息:%(message)s')
            #设置输出日志的容器，控制台和指定文件
            #输出到控制台
            sh=logging.StreamHandler()
            sh.setFormatter(formater)
            #设置日志输出的时间
            log_date=time.strftime('%y-%m-%d_%H_%M_%S')
            #设置日志输出名称
            logname=self.log_path+'/Autotest_api_{0}.log'.format(log_date)
            #输出到指定文件
            fh=logging.FileHandler(logname,'a',encoding='utf-8')
            #设定日志输出格式
            fh.setFormatter(formater)
            #设置日志输出级别
            sh.setLevel('ERROR')
            fh.setLevel('DEBUG')
            #与日志收集器进行对接
            logger.addHandler(sh)
            logger.addHandler(fh)
            #根据日志级别来输出日志
            if level=='debug':
                logger.debug(msg)
            elif level=='info':
                logger.info(msg)
            elif level=='warning':
                logger.warning(msg)
            elif level=='error':
                logger.error(msg)
            elif level=='critical':
                logger.critical(msg)
            #断开日志收集器的连接,移除日志收集器
            logger.removeHandler(sh)
            logger.removeHandler(fh)
    #根据日志级别来调用函数输出日志
    def debug(self,msg):
        self.get_log('debug',msg)
    def info(self,msg):
        self.get_log('info',msg)
    def warning(self,msg):
        self.get_log('warning',msg)
    def error(self,msg):
        self.get_log('error',msg)
    def critical(self,msg):
        self.get_log('critical',msg)
