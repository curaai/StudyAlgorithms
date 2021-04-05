import operator

class Calculator(object):
    def evaluate(self, string):
        ops = ["*/", "+-"]

        def priority(c) -> int:
            for i, xs in enumerate(ops):
                if c in xs:
                    return i 
            return 10 

        def calc():
            def cvt_op(op):
                if op == '*':
                    return operator.mul
                elif op == '/':
                    return operator.truediv
                elif op == '+':
                    return operator.add
                elif op == '-':
                    return operator.sub
                else:
                    raise IndexError("unknown item" + op)

            op = cvt_op(op_stack.pop())
            r, l = n_stack.pop(), n_stack.pop()
            n_stack.append(op(l, r))
        
        n_stack = []
        op_stack = []
        
        for x in string.split(' '):
            if x[0].isdigit():
                n_stack.append(float(x))
            elif x == '(':
                op_stack.append(x)
            elif x == ')':
                while len(op_stack) and op_stack[-1] != '(':
                    calc()
                op_stack.pop()
            else:
                while len(op_stack) and priority(x) >= priority(op_stack[-1]):
                    calc()
                op_stack.append(x)

        while len(op_stack):
            calc()
        
        if n_stack:
            return n_stack.pop()
        else:
            return 0


import unittest


class TestCalc(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(Calculator().evaluate("2 / 2 + 3 * 4 - 6"), 7)
        self.assertEqual(Calculator().evaluate("3 * 4 + 3 * 7 - 6"), 27)
        self.assertEqual(Calculator().evaluate('1 + 1'), 2)
        self.assertEqual(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"), 2)
        self.assertEqual(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"), 5)
        self.assertEqual(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"), 16)
        self.assertEqual(Calculator().evaluate("3 * ( 4 + 7 ) - 6"), 27)


if __name__ == '__main__':
    unittest.main()
