module Change where

import Data.List
import Test.HUnit

countChange :: Integer -> [Integer] -> Integer
countChange charge coins' = f (length coins) charge
  where
    coins = sort coins'
    f count left
      | left == 0 = 1
      | left < 1 = 0
      | count <= 0 && 1 <= left = 0
      | otherwise = f (count - 1) left + f count (left - coins !! (count -1))

countChange2 :: Integer -> [Integer] -> Integer
countChange2 0 xs = 1
countChange2 n [] = 0
countChange2 n (x : xs) = sum [countChange2 m xs | m <- [n, n - x .. 0]]

test1 = TestCase $ assertEqual "1" 3 (countChange2 4 [1, 2])

test2 = TestCase $ assertEqual "2" 4 (countChange2 10 [5, 2, 3])

main = runTestTT $ TestList [test1, test2]
