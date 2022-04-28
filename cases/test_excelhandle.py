#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#@Time      :2022/4/24 22:52
#@Author    :xiaoxin
#@File      :test_excelhandle.py
'''
from common.handel_excel import HandleExcel

class TestHandleExcel():
    excel = HandleExcel(r'E:\Sosuke\data\raw_meat.xlsx','预拌粉')
    cases = excel.read_excel()

    def test_case(self):
        print(self.cases)

a= TestHandleExcel()
a.test_case()