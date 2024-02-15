module PyramidSlideDown where

-- first 
longestSlideDown :: [[Int]] -> Int
longestSlideDown = head . foldr1 f 
  where 
    reduce xs = map (\i -> max (xs!!i) (xs!!(i+1))) [ 0 .. (length xs)-2]
    f smaller larger = zipWith (+) smaller $ reduce larger

-- second 
longestSlideDown_ :: [[Int]] -> Int
longestSlideDown_ = head . foldr1 f 
  where 
    f ys xs = zipWith3 (\a b c -> a + max b c) ys xs (tail xs)