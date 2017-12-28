#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 下午1:07
# @Author  : Dirk Zhao
from railway import search as se
from prettytable import PrettyTable
from railway import station_name as st


def com():
    com1 = se.cli(st_station='辛集南', des_station='济南西',)
    com2 = se.cli(st_station='济南西', des_station='上海虹桥',)
    pt = PrettyTable()
    pt._set_field_names('1车次 辛集南发车时间 济南西到达时间 2车次 济南西发车时间 上海虹桥到达时间'.split())
    for arr_times in com1:
        arr_time = arr_times[9]
        arr_int = int(arr_time[0:2]+arr_time[3:5])
        for st_times in com2:
            st_time = st_times[8]
            st_int = int(st_time[0:2]+st_time[3:5])
            if 15 < st_int-arr_int < 45:
                pt.add_row([
                    arr_times[3],
                    arr_times[8],
                    arr_times[9],
                    st_times[3],
                    st_times[8],
                    st_times[9]
                ])
            else:
                pass
    print(pt)


if __name__ == '__main__':
    com()
