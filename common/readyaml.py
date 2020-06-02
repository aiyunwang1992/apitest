# !/usr/bin/python
# -*- encoding: utf-8 -*-
# 读取yaml数据方法
import yaml


class ReadYaml():
    def read_yaml(self, filepath):
        with open(filepath, encoding='utf-8') as file:
            value = yaml.safe_load(file)
        return value


if __name__ == '__main__':
    a = ReadYaml().read_yaml(r'D:\xiazai\python\project\pyauto_apitest\lianxi\text.yaml')
    print(eval(a['check_success_msg']))
