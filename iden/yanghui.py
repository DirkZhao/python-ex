#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 下午1:49
# @Author  : Dirk Zhao


def triangles():
    l = [1]
    while True:
        yield l
        l = [1]+[l[i]+[l[i+1]] for i in range(len(l)-1)] + [1]