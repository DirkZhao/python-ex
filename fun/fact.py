#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 上午10:40
# @Author  : Dirk Zhao


def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)


hanoi(6, 'A', 'B', 'C')