def first_solution(s: str) -> int:
    valid = [False] * len(s)
    while True:
        left = [x for x in range(len(s)) if not valid[x]]
        if len(left) < 2:
            break
        
        matched = filter(lambda t: s[t[0]] == '(' and s[t[1]] == ')', zip(left, left[1:]))
        res = next(matched, None)
        if res is None:
            break
        else:
            valid[res[0]] = True
            valid[res[1]] = True
            
    _max = 0
    cur = 0
    for x in valid:
        if x:
            cur += 1
        else:
            cur = 0 
        _max = max(_max, cur)

    return _max

def second_solution(s: str) -> int:
    valid = [False] * len(s)
    stack = []
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif stack and ch == ')':
            valid[stack.pop()] = 1
            valid[i] = 1
            
    res, cur = 0, 0
    for x in valid:
        if x:
            cur += 1
        else:
            cur = 0 
        res = max(res, cur)

    return res

first_solution("(()")