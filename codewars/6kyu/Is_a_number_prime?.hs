module IsPrime where

isPrime :: Integer -> Bool
isPrime x
  | x <= 1 = False
  | x == 2 = True
  | even x = False
  | otherwise = null $ take 1 [d | d <- [3, 5 .. _max x + 1], x `mod` d == 0]
  where
    _max = floor . sqrt . fromInteger

-- >>> isPrime 10
-- False
