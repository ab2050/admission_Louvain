import unittest
from Q1adm import mtl
class test(unittest.TestCase):
    def test_mtl_1(self):
        adm = [
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        adl = [[1, 3],[2],[0],[4],[3],[]]
        self.assertEqual(mtl(adm), adl)
    
    def test2(self):
        adm2 = [
            [0, 1, 1],
            [1, 0, 0],
            [0, 0, 0]
        ]
        adl2 = [[1, 2],[0],[]]
        self.assertEqual(mtl(adm2), adl2)

if __name__ == '__main__':
    unittest.main()
