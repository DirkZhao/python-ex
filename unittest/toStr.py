#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 下午3:32
# @Author  : Dirk Zhao
import unittest


def to_str(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode('utf-8')
    else:
        raise TypeError('Must supply str or bytes, found:{}'.format(type(data)))


class TestToStr(unittest.TestCase):
    def test_str(self):
        self.assertEqual('hello', to_str('hello'), '测试通过')

    def test_bytes(self):
        self.assertEqual('hello', to_str(b'hello'), 'test right')

    # def test_else(self):
    #    self.assertEqual(TypeError, to_str, object())


if __name__ == '__main__':
    TestToStr()