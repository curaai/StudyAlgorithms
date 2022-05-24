{-# LANGUAGE DuplicateRecordFields #-}
{-# LANGUAGE FlexibleInstances #-}
{-# LANGUAGE UndecidableInstances #-}

module Main where

import Data.Bool (bool)
import Data.List (subsequences)
import GHC.Exts (sortWith)
import Test.HUnit
  ( Test (TestCase, TestLabel, TestList),
    assertEqual,
    runTestTT,
  )

nonDivisibleSubset' k s = length . head . filter isNotDivisible . reverse . sortWith length . subsequences $ s
  where
    isNotDivisible s = all f $ combination 2 s
    f = (/= 0) . (`mod` k) . sum
    combination k = filter ((== k) . length) . subsequences

nonDivisibleSubset :: Int -> [Int] -> Int
nonDivisibleSubset k s = a + b + c
  where
    a = min 1 (hist !! 0)
    b = bool 0 (min 1 (hist !! (k `div` 2))) $ even k
    c = sum [max (hist !! i) (hist !! (k - i)) | i <- [1 .. ((k -1) `div` 2)]]
    hist = let mods = map (`mod` k) s in [length . filter (== i) $ mods | i <- [0 .. (k -1)]]

tests =
  TestList
    [ TestCase $ assertEqual "a" 3 $ nonDivisibleSubset 3 [1, 7, 2, 4],
      TestCase $ assertEqual "b" 11 $ nonDivisibleSubset 7 [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436],
      TestCase $ assertEqual "c" 5 $ nonDivisibleSubset 5 [2, 7, 12, 17, 22],
      TestCase $ assertEqual "d" 5 $ nonDivisibleSubset 9 [422346306, 940894801, 696810740, 862741861, 85835055, 313720373]
    ]

main = runTestTT tests
