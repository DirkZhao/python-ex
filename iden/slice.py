#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 上午11:17
# @Author  : Dirk Zhao


def trim(s):
    while s[:1] == " ":
        s = s[1:]
    while s[-1:] == " ":
        s = s[:-1]
    return s


print(trim('  my name is dk    '))