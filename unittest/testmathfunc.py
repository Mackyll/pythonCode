import unittest
from unittest.mathfunc import *


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def testadd(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(4, add(2, 2))

    def testminus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def testmulti(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    def testdivide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))
#每一个case执行之前都会调用
    def setUp(self):
        print("every case begin init")
        pass
#每一个case执行完毕都会调用
    def tearDown(self):
        print("every case exit process")
#所有case执行之前调用，只调用一次
    @classmethod
    def setUpClass(cls):
        pass
#所有case执行之后都会调用，只调用一次
    @classmethod
    def tearDownClass(cls):
        print("all case done exit process")
        pass
