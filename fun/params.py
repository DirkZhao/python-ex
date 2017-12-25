#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 上午10:36
# @Author  : Dirk Zhao

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数


def product(*numbers):
    s = 1
    for i in numbers:
        s *= i
    return s


print(product(1, 2, 3))
print(product(1))
print(product(10, 239, 2.1))