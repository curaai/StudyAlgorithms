# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python 
# Snail 

import unittest

'''
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
---
[6 9]
[5 8]
[4 7]
---
[8 7]
[5 4]
---
[4]
[5]
---
[5]
'''

def snail(arr) -> list:
    def rotate_ccw(arr):
        return list(zip(*arr))[::-1]
    if arr == []:
        return []
    else:
        top_row = list(arr.pop(0))
        return top_row + snail(rotate_ccw(arr))



def snail2(arr) -> list:
    class Orientation:
        RIGHT=0
        DOWN=1
        LEFT=2
        UP=3

        cur = RIGHT

        def next(self):
            self.cur = (self.cur + 1) % 4
        def orientation(self):
            if self.cur == self.RIGHT:
                return 0, 1 
            elif self.cur == self.DOWN:
                return 1, 0 
            elif self.cur == self.LEFT:
                return 0, -1 
            elif self.cur == self.UP:
                return -1, 0 

    i, j = 0, 0 
    side_length = len(arr[0])

    cur_length = side_length
    count = 1

    ori = Orientation()

    res = list()
    while cur_length != 0:
        for n in range(cur_length):
            res.append(arr[i][j])
            if n == cur_length-1:
                ori.next()

            next_ori = ori.orientation()
            i, j = i + next_ori[0], j + next_ori[1]
            
        count += 1
        if count == 2:
            count = 0
            cur_length -= 1

    return res

class TestSnail(unittest.TestCase):
    def testcase1(self):
        array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(snail(array), expected)

    def testcase2(self):
        array = [[1,2,3],
                [8,9,4],
                [7,6,5]]
        expected = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(snail(array), expected)

if __name__ == "__main__":
    unittest.main()