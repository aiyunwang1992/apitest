# !/usr/bin/python3

# -*- encoding: utf-8 -*-
# !/usr/bin/python
# 正则表达式提取器
import re
from common.save_value import SaveValue


class Regular():
    # 将正则表达式匹配到的字符串进行替换
    # 注意：param这里需要传入带引号的方式传入字符串才可替换，不然会报错
    # search的用法是返回正则表达式匹配的第一个内容
    def regular(self, old_str, new_str, param):
        old_str = str(old_str)
        if re.search(old_str, str(param)) != None:
            reslut = re.sub(old_str, new_str, param)
            return reslut
        else:
            return param


if __name__ == '__main__':
    reg = Regular()
    b = "{ 'ticket':'TICKETS', 'code':123456}"
    print(reg.regular('TICKETS', SaveValue.TICKET, b))
