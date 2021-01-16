# https://www.codewars.com/kata/5541f58a944b85ce6d00006a
# Product of consecutive Fib numbers

def productFib(prod):
    prev = 0 
    n = 1
    while prev * n < prod:
        temp = n
        n = prev + n
        prev = temp

    return [prev, n, prod == prev * n]
