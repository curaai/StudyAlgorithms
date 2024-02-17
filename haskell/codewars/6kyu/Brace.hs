module Brace where

-- first answer
validBraces' xs = null $ foldl f [] xs
  where
    f :: String -> Char -> String
    f acc next
      | null acc = [next]
      | (reverseBrace . last) acc == next = init acc
      | otherwise = acc ++ [next]
    reverseBrace '(' = ')'
    reverseBrace '{' = '}'
    reverseBrace '[' = ']'
    reverseBrace _ = '_'

-- second answer
validBraces xs = null . foldr f []
  where
    f '(' (')':xs) = xs
    f '{' ('}':xs) = xs
    f '[' (']':xs) = xs
    f x xs = x:xs
