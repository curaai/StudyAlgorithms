{-# LANGUAGE DuplicateRecordFields #-}
{-# LANGUAGE FlexibleInstances #-}
{-# LANGUAGE UndecidableInstances #-}

module Main where

import Data.List (transpose)
import Data.Text (pack, stripEnd, stripStart, unpack)
import GHC.Base (undefined)
import System.Environment (getEnv)
import System.IO
  ( IOMode (WriteMode),
    hClose,
    hFlush,
    hPrint,
    openFile,
  )

formingMagicSquare :: [[Int]] -> Int
formingMagicSquare s = minimum $ map (diff s) allcases
  where
    allcases = let a = take 4 (iterate rot90 completeArray) in a ++ map transpose a
    completeArray =
      [ [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
      ]
    rot90 = map reverse . transpose
    diff a b = sum . map abs $ zipWith (-) (concat a) (concat b)

main :: IO ()
main = do
  stdout <- getEnv "OUTPUT_PATH"
  fptr <- openFile stdout WriteMode

  sTemp <- readMultipleLinesAsStringArray 3
  let s = map (map (read :: String -> Int) . words . rstrip) sTemp

  let result = formingMagicSquare s

  hPrint fptr result

  hFlush fptr
  hClose fptr
  where
    rstrip = unpack . stripEnd . pack

    readMultipleLinesAsStringArray 0 = return []
    readMultipleLinesAsStringArray n = do
      line <- getLine
      rest <- readMultipleLinesAsStringArray (n - 1)
      return (line : rest)