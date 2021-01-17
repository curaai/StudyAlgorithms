# https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python
# Sum by Factors 

import unittest
from collections import defaultdict
from typing import List
from operator import itemgetter



def sum_for_list(lst: List[int]) -> List[list]:
    def get_prime_factors(n):
        def is_prime(n):
            if n == 2:
                return True 
            elif n % 2 == 0 or n == 1:
                return False
            else:
                return not any(filter(lambda i: n % i == 0,
                            range(3, int(n ** 0.5 + 1), 2)))
        
        return list(set(
            filter(is_prime, 
            filter(lambda i: not n % i, 
                range(1, abs(n)+1)))))
    
    factor_table = defaultdict(int)
    for n in lst: 
        for f in get_prime_factors(n):
            factor_table[f] += n

    return sorted(map(list, factor_table.items()), key=itemgetter(0))


class TestSum(unittest.TestCase):
    def testcase1(self):
        a = [12, 15]
        self.assertEqual(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])
    
    def testcase2(self):
        a = [151, -199, -136, -21, -160, 88, -145, -69, -31]
        expect = [[2, -208], [3, -90], [5, -305], [7, -21], [11, 88], [17, -136], [23, -69], [29, -145], [31, -31], [151, 151], [199, -199]]
        self.assertEqual(sum_for_list(a), expect)

    def testcase3(self):
        a =  [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
        expect = [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]]
        self.assertEqual(sum_for_list(a), expect)

    def testcase4(self):
        a =  [15, 21, 24, 30, -45]
        expect =  [[2, 54], [3, 45], [5, 0], [7, 21]]
        self.assertEqual(sum_for_list(a), expect)

    def testcase5(self):
        a = [108, -178, -115, -12, -153, 67, -75, -167, -149, -169, 26, -46, -52, -167]
        expect = [[2, -154], [3, -132], [5, -190], [13, -195], [17, -153], [23, -161], [67, 67], [89, -178], [149, -149], [167, -334]]
        self.assertEqual(sum_for_list(a), expect)

if __name__ == "__main__":
    unittest.main()