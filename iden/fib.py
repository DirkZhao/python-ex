#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 下午1:35
# @Author  : Dirk Zhao


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield(b)
        a, b = b, a+b
        n = n+1
    return 'done'


for n in fib(5):
    print(n)