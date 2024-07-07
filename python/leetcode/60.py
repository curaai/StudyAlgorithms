import math
from typing import List
import unittest

class Test(unittest.TestCase):
    def test_a(self):
        self.assertEqual(getPermutation(3,3), "213")
        self.assertEqual(getPermutation(4,9), "2314")
        self.assertEqual(getPermutation(3,1), "123")
        self.assertEqual(getPermutation(3,2), "132")
        self.assertEqual(getPermutation(2,2), "21")

def getPermutation(n: int, k: int) -> str:
    numbers = list(range(1, n+1))
    res = ''
    k -= 1
    while 0 < n:
        n -= 1
        idx, k = divmod(k, math.factorial(n))
        res += str(numbers.pop(idx))
    return res

def getPermutation(n: int, k: int) -> str:
    def f(k: int, nums: List[int]) -> str:
        if not nums: return ""
        i, k = divmod(k, math.factorial(len(nums)-1))
        return str(nums.pop(i)) + f(k, nums)
    
    return f(k-1, list(range(1, n+1)))

unittest.main()