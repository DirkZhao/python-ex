#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 下午3:18
# @Author  : Dirk Zhao
import sys


class Chain(object):
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, name):
        return Chain('%s/%s'(self._path, name))

    __repr__ = __str__

    sys.setrecursionlimit(100000)


print(Chain().status)