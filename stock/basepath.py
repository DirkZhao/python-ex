#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 13:35
# @Author  : Dirk Zhao
import os


def base_path(base_name):
    curdir = os.path.abspath(os.path.curdir)
    dirlist = curdir.split(os.path.sep)
    path = ''
    for dir in dirlist[1:]:
        path = path + os.path.sep + dir
        if dir == base_name:
            return path
            break


BASE_PATH = base_path('python-ex')
print(BASE_PATH)