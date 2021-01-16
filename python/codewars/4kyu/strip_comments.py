# https://www.codewars.com/kata/51c8e37cee245da6b40000bd
# Strip Comments

def solution(string,markers):
    res = ''
    i = 0
    ignore = False
    while i < len(string):
        char = string[i]

        if char in markers:
            ignore = True
        elif char == '\n':
            ignore = False

        if not ignore:
            res += char
        
        i += 1
    return '\n'.join(map(str.strip, res.split('\n')))