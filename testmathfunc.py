import unittest
from mathfunc import *


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

