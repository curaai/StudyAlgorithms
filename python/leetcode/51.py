from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    res = [] 

    def to_string(queens):
        return list(map(lambda q: '.' * q[1] + 'Q' + '.' * (n-q[1]-1), queens))
 
    def tracking(queens, cols):
        if len(queens) == n:
            return res.append(queens)

        row = len(queens)
        for col in range(n):
            if col in cols:
                continue 

            if any(map(lambda q: abs(q[0] - row) == abs(q[1] - col), queens)):
                continue

            tracking(queens+[(row, col)], cols+[col])
            

    for i in range(n):
        queens = [(0, i)]

        tracking(queens, [i])
    
    return list(map(to_string, res))
    
print(solveNQueens(4))
