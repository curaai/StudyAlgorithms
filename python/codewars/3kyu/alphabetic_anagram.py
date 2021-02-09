# https://www.codewars.com/kata/53e57dada0cb0400ba000688/train/python
# Alphabetic Anagrams 

from operator import mul, floordiv, itemgetter
from functools import reduce
from collections import Counter

def listPosition(s):
    def all_cnt(c):
        f = lambda n: reduce(mul, range(1, n+1))
        return reduce(floordiv, map(f, c.values()), f(sum(c.values())))

    if not s:
        return 1 

    c = Counter(s)

    res = 0
    for x in sorted(list(set(c))):
        if x == s[0]:
            return res + listPosition(s[1:])
        res += int(all_cnt(c - Counter(x)))

import unittest
class TestAnagram(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(listPosition('A'), 1)
        self.assertEqual(listPosition('QUESTION'), 24572)

    def test_dup_alphabet(self):
        self.assertEqual(listPosition('ABAB'), 2)
        self.assertEqual(listPosition('BOOKKEEPER'), 10743)
        self.assertEqual(listPosition('AAAB'), 1)
        self.assertEqual(listPosition('BAAA'), 4)
        self.assertEqual(listPosition('IMMUNOELECTROPHORETICALLY'), 718393983731145698173)

if __name__ == "__main__":
    unittest.main()
