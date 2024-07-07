def totalNQueens( n: int) -> int:
    def tracking(queens, cols):
        if len(queens) == n:
            return 1

        row = len(queens)
        res = 0
        for col in range(n):
            if col in cols:
                continue 

            if any(map(lambda q: abs(q[0] - row) == abs(q[1] - col), queens)):
                continue

            res += tracking(queens+[(row, col)], cols+[col])
        return res

    return sum(map(lambda i: tracking([(0, i)], [i]), range(n)))
