#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/27 下午5:19
# @Author  : Dirk Zhao
import requests
from railway import station_name as st
from prettytable import PrettyTable
from urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def cli(st_station='上海', des_station='辛集', date: object = '2018-09-01') -> object:
    from_station = st.get_code(st_station)
    to_station = st.get_code(des_station)
    url = ('https://kyfw.12306.cn/otn/leftTicket/query?'  
            'leftTicketDTO.train_date={}&'  
            'leftTicketDTO.from_station={}&'  
            'leftTicketDTO.to_station={}&'  
            'purpose_codes=ADULT').format(date, from_station, to_station)

    r = requests.get(url, verify=False)
    # print(r.json())
    raw_trains = r.json()['data']['result']
    # print(raw_trains)
    pt = PrettyTable()
    data_lists =[]
    pt._set_field_names("车次   车站    发车时间  到达时间   经历时 一等座 二等座  软卧  硬卧  硬座  无座".split())
    for raw_train in raw_trains:
        data_list = raw_train.split("|")
        data_lists.append(data_list)
        train_no = data_list[3]  # 车次
        from_station_name = st_station
        start_time = data_list[8]  # 发车时间
        arrive_time = data_list[9]  # 到达时间
        time_duration = data_list[10]  # 经历时间
        first_class_seat = data_list[31] or "--"
        second_class_seat = data_list[30] or "--"
        soft_sleep = data_list[23] or "--"
        hard_sleep = data_list[28] or "--"
        hard_seat = data_list[29] or "--"
        no_seat = data_list[33] or "--"
        pt.add_row([
            train_no,
            from_station_name,
            start_time,
            arrive_time,
            time_duration,
            first_class_seat,
            second_class_seat,
            soft_sleep,
            hard_sleep,
            hard_seat,
            no_seat
            ])
    # print(data_lists)
    print(pt)
    return data_lists


if __name__ == '__main__':
    cli()
