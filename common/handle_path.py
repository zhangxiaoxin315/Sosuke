#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#@Time      :2022/4/28 21:16
#@Author    :xiaoxin
#@File      :handle_path.py
用于处理项目中的绝对路径
'''

import os
#项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#配置文件根目录
CONF_DIR = os.path.join(BASE_DIR,"config")
#日志文件所在目录
LOG_DIR = os.path.join(BASE_DIR,"logs")
#用例所在目录
CASES_DIR = os.path.join(BASE_DIR,"cases")
