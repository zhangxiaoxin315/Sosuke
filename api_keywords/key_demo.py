#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#@Time      :2021/10/19 20:44
#@Author    :xiaoxin
#@File      :key_demo.py
'''
import requests


class KeyDemo:

    # def get(self,url,headers=None,param=None):
    #     return requests.get(url=url,headers=headers,params=param)
    #
    # def post(self,url,headers=None,data=None):
    #     return requests.post(url=url,headers=headers,data=data)


    def __init__(self):
        self.session = requests.session()
    def request_send(self,url,method,params=None,data=None,json=None,headers=None,**kwargs):
        try:
            return self.session.request(url=url,method=method,params=params,data=data,json=json,headers=headers,**kwargs)
        except ValueError as err:
            return "请求错误{}".format(err)

if __name__ == '__main__':
    url = "http://www.baidu.com"
    method = "GEt"
    r = KeyDemo().request_send(url=url,method=method)
    print(r.text)
