module Codewars.G964.Longest where

import Data.List
import Data.Set

longest :: [Char] -> [Char] -> [Char]
longest s1 s2 = sort . nub $ s1 ++ s2

a = "xyaabbbccccdefww"

b = "xxxxyyyyabklmopq"

-- >>> longest a b
-- "abcdefklmopqwxy"
