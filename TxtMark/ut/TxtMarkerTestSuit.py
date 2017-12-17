import unittest
from TxtMark.ut.TxtMarkerTest import TxtMarkerCase

if __name__ == "__main__":
    suit = unittest.TestSuite()
    Tests = ["TxtMarkerTest.TxtMarkerCase"]
    suit.addTests(unittest.TestLoader().loadTestsFromNames(Tests))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)
