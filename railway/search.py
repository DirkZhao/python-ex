#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/27 下午5:19
# @Author  : Dirk Zhao
"""命令行火车票查看器:Usage　Options为docopt库固定格式

Usage:
    tickets [-dgktz] <from> <to> <date>

Options:
    -h, --help 查看帮助
    -d         动车
    -g         高铁
    -k         快速
    -t         特快
    -z         直达

Examples:
    tickets 上海 北京 2017-10-10
    tickets -dg 成都 南京 2017-10-10
"""
from docopt import docopt
import requests
from prettytable import PrettyTable
from colorama import Fore
from railway import station_name as st
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def cli():
    arguments = docopt(__doc__, version='ticket 1.0')
    # from_station = st.get_code(arguments.get('<from>'))
    from_station = 'JGK'
    # to_station = st.get_code(arguments.get('<to>'))
    to_station = 'SHH'
    # date = arguments.get('<date>')
    date = '2017-12-31'
    # 列表推导式，得到的是查询车次类型的集合
    options = ''.join([key for key, value in arguments.items() if value is True])
    print(options)

    url = ('https://kyfw.12306.cn/otn/leftTicket/query?'  
            'leftTicketDTO.train_date={}&'  
            'leftTicketDTO.from_station={}&'  
            'leftTicketDTO.to_station={}&'  
            'purpose_codes=ADULT').format(date, from_station, to_station)

    r = requests.get(url, verify=False)
    raw_trains = r.json()['data']['result']
    # print(raw_trains)
    pt = PrettyTable()
    pt._set_field_names("车次 车站 时间 经历时 一等座 二等座 软卧 硬卧 无座".split())
    # for raw_train in raw_trains:
