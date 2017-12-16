import unittest
from testmathfunc import TestMathFunc

if __name__ == "__main__":
    suite = unittest.TestSuite()
    Tests = [TestMathFunc("testadd"), TestMathFunc("testminus"), TestMathFunc("testmulti")]
    suite.addTests(Tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
