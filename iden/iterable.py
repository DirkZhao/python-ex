#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 下午1:14
# @Author  : Dirk Zhao

from collections import Iterable
# isinstance('abcdf', Iterable)


def findmaxandmin(l):
    max = l[0]
    min = l[0]
    for x in l:
        if x<min:
            min=x
        if x>max:
            max=x
    return print('最小值是'+min,'\n最大值是'+max)

findmaxandmin([1,2,312,42,5,6,12,31,])