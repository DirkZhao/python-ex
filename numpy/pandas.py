#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 14:25
# @Author  : Dirk Zhao
from pandas import Series, DataFrame
import pandas as pd

s = Series([100, 'python', float(2.299)], index=[2,4,6])
print(s)
