module Tribonacci where


tribonacci :: Num a => (a, a, a) -> Int -> [a]
tribonacci _ n | n < 1 = []
tribonacci (a, b, c) n = a : tribonacci (b, c, a+b+c) (n-1)

tribonacci1 :: Num a => (a, a, a) -> Int -> [a]
tribonacci1  (a, b, c) n = take n $ [a,b,c] ++ func [a, b, c] 

func [x, y, z] = next:func [y, z, next]
    where next = x + y + z