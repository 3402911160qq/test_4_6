# -*- coding: utf-8 -*-
# Time :2023/2/16 14:41
# Author : daidai
# File :test_script4-3-01.PY
# Desc :
import pytest

class TestCases1:
    def test_1(self):
        print('第一个测试用例')

    def test_2(self):
        print('第二个测试用例')



if __name__ == '__main__':
    pytest.main(['-s','-v'])

