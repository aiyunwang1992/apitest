# !/usr/bin/python
# -*- encoding: utf-8 -*-
# 读取配置文件的模块
import configparser


class Config():
    ''' 读取配置文件 '''

    def configer(self, filepath, section, option):
        """

        :param filepath:
        :param section:
        :param option:
        :return:
        """
        # 创建读取配置文件的实例
        cf = configparser.ConfigParser()
        # 打开配置文件,并设置字符集（避免含中文字符的报错）
        cf.read(filepath, encoding='utf-8')
        # 获取配置文件的内容，并将其转换为python可识别的字符
        value = eval(cf.get(section, option))
        return value


if __name__ == '__main__':
    filepath = 'F:\python\project\jiekoutest\conf\db_config.conf'
    section = 'DB'
    option = 'db_conf'
    conf = Config().configer(filepath, section, option)
    print(conf)
