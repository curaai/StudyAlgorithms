# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python
# Sum of Intervals

from operator import itemgetter
from functools import reduce

def sum_of_intervals(l: list) -> int:
    def join(a, b):
        last = a[-1]
        if b[0] < last[1]:
            joined = [min(last[0], b[0]), max(last[1], b[1])]
            return f(a[:-1] + [joined])
        else:
            return a + [b]

    def f(l):
        l = sorted(l, key=itemgetter(1) )
        return reduce(join, l[1:], [l[0]])

    res = f(l)
    return sum(map(lambda itv: abs(itv[1] - itv[0]), res)) 


import unittest

class TestIntervals(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(sum_of_intervals( [ [1,2], [6, 10], [11, 15] ] ), 9)
        self.assertEqual(sum_of_intervals( [ [1,4], [7, 10], [3, 5] ] ), 7) 
        self.assertEqual(sum_of_intervals( [ [1,5], [10, 20], [1, 6], [16, 19], [5, 11] ] ), 19)

if __name__ == "__main__":
    unittest.main()
