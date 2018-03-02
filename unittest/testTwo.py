import unittest

class Two(unittest.TestCase):
    c = 2
    d = 6
    def testTwoOne():
        if c < d:
            print('c小于d')

    def testTwoTwo():
        if c> d:
            print('c大于d')