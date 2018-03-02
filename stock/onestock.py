#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 09:34
# @Author  : Dirk Zhao
import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import configparser
from stock.basepath import BASE_PATH
import os


# 演示基本用法
# data = ts.get_hist_data(code='600760', start=start, end=end)
# start = datetime(2018, 1, 1).strftime('%Y-%m-%d')
# end = datetime.now().strftime('%Y-%m-%d')
# data = ts.get_hist_data(code='600760', start=start, end=end)
# print(data)
# print(data['close'])
# data['close'].plot(kind='line', use_index=True, title='hello')
# plt.show()


def stocks():
    start = datetime(2018, 1, 1).strftime('%Y-%m-%d')
    end = datetime.now().strftime('%Y-%m-%d')
    cp = configparser.ConfigParser()
    file = os.path.join(BASE_PATH, 'stock', 'stock.ini')
    cp.read(file)
    stocks = cp.items('stocks')
    for name, code in stocks:
            data = ts.get_hist_data(code=code, start=start, end=end)
            # print(data)
            plt.plot(data.index, data['p_change'], label=name)
    plt.show()


stocks()