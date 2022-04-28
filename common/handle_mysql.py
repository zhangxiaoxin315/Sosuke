#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#@Time      :2022/4/28 22:54
#@Author    :xiaoxin
#@File      :handle_mysql.py
'''

import pymysql
from common.handle_config import conf

class HandleDB:
    def __init__(self):
        self.con = pymysql.connect(**conf["mysql"])

    def find_all(self, sql):
        """查询查询到的所有数据"""
        with self.con as cur:
            cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    def find_one(self, sql):
        """查询一条数据"""
        with self.con as cur:
            cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        return res

    def find_count(self, sql):
        """sql执行完之后，返回的数据条数"""
        with self.con as cur:
            res = cur.execute(sql)
        cur.close()
        return res

    def __del__(self):
        self.con.close()
