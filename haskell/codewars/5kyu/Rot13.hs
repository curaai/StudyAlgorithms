module Rot13 where

import Data.Char

rot13 :: String -> String
rot13 = map r13 
  where
    r13 x
      | not (isLetter x && isAscii x) = x
      | toLower x <= 'm' = chr $ ord x + 13
      | otherwise = chr $ ord x - 13


rot13' :: String -> String
rot13' = map cvt 
  where 
  cvt x = let _lst = lst x in if isAscii x && isLetter x then idx _lst x  else x 
  lst x = if isUpper x then ['A'..'Z'] else ['a'..'z'] 
  idx lst x = lst!!(mod ( elemIndex' (x::Char) lst + 13) 26)
  elemIndex' x lst = head [i | i <- [0..length lst], lst!!i == x]