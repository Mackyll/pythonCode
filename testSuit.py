import unittest
from testmathfunc import TestMathFunc


if __name__ == "__main__":
    suite = unittest.TestSuite()
    # 使用addTest方法添加测试用例
    Tests = [TestMathFunc("testadd"), TestMathFunc("testminus"), TestMathFunc("testmulti")]
    suite.addTests(Tests)
    suite.addTests(unittest.TestLoader().loadTestsFromName('testmathfunc.TestMathFunc'))
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['testmathfunc.TestMathFunc']))

    # loadTestsFromTestCase()，传入TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
