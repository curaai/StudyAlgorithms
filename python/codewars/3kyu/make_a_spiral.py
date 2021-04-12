import operator 


def spiralize(size):
    op = operator.__add__
    n = size-1
    arr = [[1 for _ in range(size)] for _ in range(size)]
    pos = [1, -1]

    def reverse(op):
        return operator.__sub__ if op == operator.__add__ else operator.__add__
    def iterate(axis):
        a = axis == 'x'
        for i in range(n):
            pos[a] = op(pos[a], 1)
            arr[pos[0]][pos[1]] = 0

    while 0 < n:
        iterate('x')
        n -= 2
        iterate('y')
        op = reverse(op)

    return arr



import unittest


class TestSpiral(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(spiralize(5), [[1,1,1,1,1],
                                        [0,0,0,0,1],
                                        [1,1,1,0,1],
                                        [1,0,0,0,1],
                                        [1,1,1,1,1]])
        self.assertEqual(spiralize(8), [[1,1,1,1,1,1,1,1],
                                        [0,0,0,0,0,0,0,1],
                                        [1,1,1,1,1,1,0,1],
                                        [1,0,0,0,0,1,0,1],
                                        [1,0,1,0,0,1,0,1],
                                        [1,0,1,1,1,1,0,1],
                                        [1,0,0,0,0,0,0,1],
                                        [1,1,1,1,1,1,1,1]])        

if __name__ == '__main__':
    unittest.main()