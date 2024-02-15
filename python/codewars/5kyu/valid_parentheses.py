# https://www.codewars.com/kata/52774a314c2333f0a7000688
# Valid Parentheses

def valid_parentheses(string):
    n = 0
    for x in string:
        if x == '(': n +=1 
        elif x == ')': n -= 1
        if n < 0: return False
    return n == 0

'''
class Stack:
    def __init__(self):
        self.stack = list()
        
    def push(self):
        self.stack.append(" ")
    def pop(self):
        self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
    
def valid_parentheses(string):
    s = Stack()
    
    paren = list(filter(lambda x: x in '()', string))
    for x in paren:
        if x == '(':
            s.push()
        else:
            if s.is_empty():
                return False
            s.pop()
    return s.is_empty()
'''