module Difference where

import Data.List 

difference1 a b = foldl f [] a
  where
    f res x = if x `elem` b then res else res ++ [x]

difference2 a b = filter (`notElem` b) a
