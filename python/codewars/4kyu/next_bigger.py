# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python
# Next Bigger number with same digits

from itertools import permutations 
from typing import List


def next_bigger(n) -> int:
    str_n = list(str(n))
    int_n = list(map(int, str_n))
    slist2int = lambda l: int(''.join(l))
    
    if sorted((str_n), reverse=True) == str_n:
        return -1 
    else:
        def right_smaller_idx(l: List[int]) -> int:
            prev = l[-1]
            for i, x in enumerate(reversed(l[:-1]), 2):
                if x < prev:
                    break 
                prev = x 
            return -i

        def align(l: List[str], idx) -> List[str]:
            def next_bigger_right(l: List[int], idx):
                for i, x in enumerate(reversed(l), 1):
                    if l[idx] < x:
                        return -i

            nidx = next_bigger_right(list(map(int, l)), idx)
            l[idx], l[nidx] = l[nidx], l[idx]
            l = l[:idx+1] + sorted(l[idx+1:])
            return l

        idx = right_smaller_idx(int_n)
        return slist2int(align(str_n, idx))



import unittest
class TestBigger(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(next_bigger(12),21)
        self.assertEqual(next_bigger(513),531)

    def testcase2(self):
        self.assertEqual(next_bigger(2017),2071)
        self.assertEqual(next_bigger(414),441)
        self.assertEqual(next_bigger(144),414)
    
    def testcase3(self):
        self.assertEqual(next_bigger(46541), 51446)


if __name__ == "__main__":
    unittest.main()