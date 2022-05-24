module Main where

import Data.Bool (bool)
import Data.Char (isSpace)
import Data.List.Split (chunksOf)
import Test.HUnit
  ( Counts,
    Test (TestCase, TestList),
    assertEqual,
    runTestTT,
  )

trim = f . f
  where
    f = reverse . dropWhile isSpace

encryption :: String -> String
encryption s = unwords $ map (trim . crawlChar) [0 .. col -1]
  where
    crawlChar n = map getChar rows
      where
        getChar row = bool ' ' (row !! n) (n < length row)
    rows = chunksOf col s
    col = ceiling . sqrt . fromIntegral . length $ s

test1 = TestCase $ assertEqual "main1" "clu hlt io" $ encryption "chillout"

test2 = TestCase $ assertEqual "main2" "hae and via ecy" $ encryption "haveaniceday"

main = runTestTT $ TestList [test1, test2]