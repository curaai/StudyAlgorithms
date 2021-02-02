
import unittest
from functools import reduce 
from functools import reduce 

def dirReduc(arr):
    opposite = {"NORTH": "SOUTH", "WEST": "EAST", "SOUTH": "NORTH", "EAST": "WEST"}
    def join(a: list, b: str):
        if a and opposite[a[-1]] == b:
            a.pop()
        else:
            a.append(b)
        return a

    if not arr:
        return []
    return reduce(join, arr[1:], [arr[0]])
    
    
class TestScamble(unittest.TestCase):
    def testcase1(self): 
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        self.assertEqual(dirReduc(a), ['WEST'])
        
    def testcase2(self):
        u=["NORTH", "WEST", "SOUTH", "EAST"]
        self.assertEqual(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])

if __name__ == "__main__":
    unittest.main()