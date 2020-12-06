module Codewars.Kata.SplitStrings where

solution :: String -> [String]
solution [] = []
solution [x] = [x:"_"]
solution xs = take 2 xs : solution ( drop 2 xs)