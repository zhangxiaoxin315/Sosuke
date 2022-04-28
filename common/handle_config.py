#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#@Time      :2022/4/28 21:08
#@Author    :xiaoxin
#@File      :handle_config.py
'''
import os
from configparser import ConfigParser
from common.handle_log import logger
from common.handle_path import CONF_DIR
class MyConfigParser(ConfigParser):
    def __init__(self):
        super().__init__()


    def load_ini(self,file_path):
        logger.info("加载{}文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = config._sections
        return data
my_conf = MyConfigParser()
conf = my_conf.load_ini(os.path.join(CONF_DIR,'config.ini'))