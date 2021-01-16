import unittest
from functools import reduce


# def middle_permutation(string):
#     total_n_cases = reduce(lambda a, b: a * b, range(1,len(string)+1))
#     length = len(string)

#     cases = list()
#     def f(head, last):
#         if len(cases) = 
#         if len(last) == 1:
#             cases.append(head + last) 

#         for i in range(len(last)):
#             last_ = last.copy()
#             head_ = head+ [last_.pop(i)]
#             f(head_, last_)

#     f([], list(sorted(string)))
#     res = list(map(''.join, cases))
#     return res[int(total_n_cases / 2)-1]

def longest_consec(strarr, k):
    if k < -1 or len(strarr) < k:
        return ''

    return max(
           map(''.join, 
           map(lambda i: strarr[i:i+k], 
               range(0, len(strarr)))), key=len)

class TestScamble(unittest.TestCase):
    def testcase1(self): 
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        self.assertEqual(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
        self.assertEqual(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        self.assertEqual(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
    def testcase2(self):
        self.assertEqual(longest_consec([], 3), "")
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
    def testcase3(self):
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
        

if __name__ == "__main__":
    unittest.main()