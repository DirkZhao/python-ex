#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 上午10:37
# @Author  : Dirk Zhao
import HttpClient


class TestLogin():
    def __init__(self, url):
        self.url = url
        self.hc = HttpClient.HttpClient(url=self.url)

    def request(self):
        response = self.hc.send()
        print(response)


if __name__ == '__main__':
    TestLogin(url='http://www.baidu.com').request()



