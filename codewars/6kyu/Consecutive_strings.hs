module Codewars.G964.Longestconsec where

import Data.List
import Data.Function


longestConsec arr k = head . last . groupBy (len_on (==)) $ sortBy (len_on compare) subarrs
    where len_on x = on x length
          subarrs = [arr & concat . take' k . drop i | i <- [0..length arr]]
          take' n xs = if length xs < n then [] else take n xs