# https://www.codewars.com/kata/520446778469526ec0000001/train/python/60004924231575002d1fc98b
# Nesting Structure Comparison 


def same_structure_as(a, b) -> bool:
    ta, tb = type(a), type(b)

    if ta == tb == list and len(a) == len(b):
        return all(map(same_structure_as, a, b))
    else:
        return not (ta == list or tb == list)

import unittest


class TestNested(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(same_structure_as([1,'[',']'], ['[',']',1]))
    
    def testcase2(self):
        self.assertTrue(same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ))
        self.assertTrue(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] ))
        self.assertTrue(same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] ))

    def testcase3(self):
        self.assertFalse(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ))
        self.assertFalse(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] ))
        self.assertFalse(same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] ))

if __name__ == "__main__":
    unittest.main()
