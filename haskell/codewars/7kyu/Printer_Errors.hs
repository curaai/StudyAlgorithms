module Codewars.G964.Printer where

import Data.List 

printerError :: [Char] -> [Char]
printerError s = show cnt ++ "/" ++ show (length s)
  where cnt = length $ filter ('m' <) s