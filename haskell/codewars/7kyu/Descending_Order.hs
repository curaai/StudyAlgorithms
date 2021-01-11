module DescendingOrder where

import Data.List
import Data.Ord

descendingOrder1 :: Integer -> Integer
descendingOrder1 = read . sortBy (comparing Down) . show

descendingOrder2 :: Integer -> Integer
descendingOrder2 i = read . reverse . sort . show $ i