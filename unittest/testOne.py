import unittest

class TestOne(unittest.TestCase):
    a = 1
    b = 2
    def testOneOne():
        if a>b:
            print('a大于b')
    def testOneTwo():
        if a>b:
            print('a小于b')