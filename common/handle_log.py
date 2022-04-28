#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#@Time      :2022/4/28 21:35
#@Author    :xiaoxin
#@File      :handle_log.py
'''

import logging,os,time
from configparser import ConfigParser
from common.handle_path import LOG_DIR,CONF_DIR
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)


def create_log(name='mylog', level="DEBUG", filename='log.log', sh_level='DEBUG', fh_level="DEBUG"):
    # 第一步:创建日志收集器
    log = logging.getLogger(name)

    # 第二步:设置收集器收集日志的等级
    log.setLevel(level)

    # 第三步：设置日志输出渠道
    # 3.1、输出到文件的配置
    fh = logging.FileHandler(filename, encoding="utf-8")
    fh.setLevel(fh_level)
    log.addHandler(fh)

    # 3.2、输出到控制台
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)

    # 第四步：设置日志输出的格式
    # 4、设置日志输出的等级
    formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
    # 创建格式对象
    log_format = logging.Formatter(formats)
    # 为输出渠道设置输出格式
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)

    # 返回一个日志收集器
    return log

conf = ConfigParser()
conf.read(os.path.join(CONF_DIR, 'config.ini'))

logger = create_log(
    name=conf.get("logging", 'name'),
    level=conf.get('logging', 'level'),
    filename=os.path.join(LOG_DIR, "{}.log".format(time.strftime("%Y%m%d"))),
    sh_level=conf.get('logging', 'sh_level'),
    fh_level=conf.get('logging', 'fh_level'),
)
