# https://www.codewars.com/kata/52ec24228a515e620b0005ef/train/python
# Explosive Sum 

import unittest

'''
exp_sum(1) # 1
exp_sum(2) # 2  -> 1+1 , 2
exp_sum(3) # 3 -> 1+1+1, 1+2, 3
exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3
'''

from collections import defaultdict
cache = defaultdict(dict)

def exp_sum(n):
    return sum(map(lambda k: partial(n, k), range(1, n+1)))

def partial(n, k):
    if k == 1 or n == k:
        return 1 
    if n < k:
        return 0
    if k in cache[n]:
        return cache[n][k]
    res = partial(n-1, k-1) + partial(n-k, k)
    cache[n][k] = res 
    return res

class TestSum(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(exp_sum(4), 5)
        self.assertEqual(exp_sum(5), 7)
        self.assertEqual(exp_sum(10), 42)

    def testcase2(self):
        self.assertEqual(exp_sum(1), 1)
        self.assertEqual(exp_sum(2), 2)
        self.assertEqual(exp_sum(3), 3)

if __name__ == "__main__":
    unittest.main()