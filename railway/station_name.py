#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/27 下午4:36
# @Author  : Dirk Zhao
import re
import requests
from urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_code(name):
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9039'
    r = requests.get(url, verify=False)
    stations = dict(re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', r.text))
    namelist = []
    for k, v in stations.items():
        namelist.append(k)
        namelist.append(v)
    # print(stations)
    if not isinstance(name, str):
        print("需要输入字符串类型的站名")
    elif name not in namelist:
        print("没有该车站名，请核对后再次查询")
    else:
        code = stations[name]
        return code
    # print(code)