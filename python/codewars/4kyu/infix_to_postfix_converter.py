def to_postfix (infix):
    ops = ["^", "*/", "+-"]
    L = lambda a, b: a>=b
    R = lambda a, b: a>b
    OP_ORDER = {"^": R, "*": L, "/": L, "+": L, "-": L}

    def priority(c) -> int:
        for i, xs in enumerate(ops):
            if c in xs:
                return i 
        return len(ops) 
    
    res, op_stack = [], []
    
    for x in infix:
        if x.isdigit():
            res.append(x)
        elif x == '(':
            op_stack.append(x)
        elif x == ')':
            while op_stack and op_stack[-1] != '(':
                res.append(op_stack.pop())
            op_stack.pop()
        else:
            while op_stack and OP_ORDER[x](priority(x), priority(op_stack[-1])):
                res.append(op_stack.pop())
            op_stack.append(x)

    return ''.join(res + op_stack[::-1])


import unittest


class TestConverter(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(to_postfix("2+7*5"), "275*+")
        self.assertEqual(to_postfix("3*3/(7+1)"), "33*71+/")
        self.assertEqual(to_postfix("5+(6-2)*9+3^(7-1)"), "562-9*+371-^+")
        self.assertEqual(to_postfix("(5-4-1)+9/5/2-7/1/7"), "54-1-95/2/+71/7/-")
        self.assertEqual(to_postfix("1^2^3"), "123^^")
    
if __name__ == '__main__':
    unittest.main()