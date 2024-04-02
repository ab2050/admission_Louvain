import unittest
from Q2adm import reach

class test(unittest.TestCase):
    def test1(self):
        adl = [[1, 3], [2], [0], [4], [3], []]
        n = 0
        res = {0, 1, 2, 3, 4}
        self.assertEqual(reach(adl, n), res)

    def test2(self):
        adl = [[1, 3], [2], [0], [4], [3], []]
        n = 5
        res = {5}
        self.assertEqual(reach(adl, n), res)

if __name__ == '__main__':
    unittest.main()