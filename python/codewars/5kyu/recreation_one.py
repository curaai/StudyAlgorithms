# https://www.codewars.com/kata/55aa075506463dac6600010d
# Integers: Recreation One

import math 

def list_squared(m, n):
    square_cash = dict()
    def get_factors(n):
        res = [1, n]
        for i in range(2, round(math.sqrt(n)) + 1):
            quotient, remainder = divmod(n, i)
            if remainder == 0:
                res += [i, quotient]
        return list(set(res))

    def get_squares(factors) -> list:
        def get_square(x):
            if x in square_cash:
                return square_cash[x]
            else:
                res = x ** 2
                square_cash[x] = res 
                return res

        return list(map(get_square, factors))

    res = []
    for i in range(m, n+1):
        sum_ = sum(get_squares(get_factors(i)))
        if math.sqrt(sum_).is_integer():
            res.append([i, sum_])
    return res 