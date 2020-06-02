# !/usr/bin/python
# -*- encoding: utf-8 -*-
# 使用fixture
import pytest
from common.read_apidata import ReadData

test_datas = ReadData().read_data()
print(test_datas)


@pytest.fixture(params=test_datas)
def param(request):
    return request.param
