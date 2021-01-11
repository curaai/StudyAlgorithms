module MaxSequence where

import Data.Function
import Data.List 

-- Return the greatest subarray sum within the array of integers passed in.

maxSequence :: [Int] -> Int
maxSequence s  
  | null s = 0
  | otherwise = (\x -> if x < 0 then 0 else x) . sum $ maximumBy (compare `on` sum) subseq 
    where 
      _tails = init . tails $ s
      subseq = _tails ++ concatMap (init . inits) _tails