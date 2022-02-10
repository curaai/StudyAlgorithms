module RangeExtractor where

import Data.List
import Test.HUnit

solution1 xs = intercalate "," $ map toString $ foldl f [(head xs, head xs)] (tail xs)
  where
    toString (x, y)
      | x == y = show x
      | y - x < 2 = show x ++ "," ++ show y
      | otherwise = show x ++ "-" ++ show y
    f res a = init' ++ if ((== 1) . abs . (-) a . snd) last' then [(fst last', a)] else [last', (a, a)]
      where
        init' = init res
        last' = last res

solution2 :: [Integer] -> String
solution2 = intercalate "," . map showRange . foldr mkRange []
  where
    mkRange x ((a, b) : xs) | a - x == 1 = (x, b) : xs
    mkRange x xs = (x, x) : xs
    showRange (x, y) = case y - x of
      0 -> show x
      1 -> show x ++ "," ++ show y
      _ -> show x ++ "-" ++ show y

test1 = TestCase $ assertEqual "1" "-10--8,-6,-3-1,3-5,7-11,14,15,17-20" (solution2 [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])

main = runTestTT $ TestList [test1]
