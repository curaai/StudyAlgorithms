module UnlimitedGameOfLife where

import Data.List (transpose)

oldAnswer arr' i
  | null arr' = arr'
  | i == 0 = arr'
  | otherwise = oldAnswer (shrink [[ f' x y | x <- [0..col]] | y <- [0..row]]) (i-1)
  where
    arr = expand arr'
    col = length (head arr) - 1
    row = length arr - 1
    f' x y
        | ((arr!!y)!!x) == 1 = if sum' == 2 || sum' == 3 then 1 else 0
        | otherwise = if sum' == 3 then 1 else 0
      where
        sum' = sum [arr!!y'!!x' |
          x' <- [max 0 (x-1) .. min col (x+1)],
          y' <- [max 0 (y-1) .. min row (y+1)],
          x' /= x || y' /= y]
    expand xss = map (\r -> [0] ++ r ++ [0]) $ [row] ++ xss ++ [row]
      where
        row = replicate (length . head $ xss) (0 :: Int)

    shrink xss 
      | null idx = []
      |otherwise = slice ymin ymax $ map (slice xmin xmax) xss
      where
        col = (+(-1)) . length . head $ xss
        row = (+(-1)) . length $ xss
        idx = [(y, x) | x <- [0 .. col], y <- [0..row], xss!!y!!x == 1]
        (xmin, xmax) = (minimum $ map snd idx, maximum $ map snd idx)
        (ymin, ymax) = (minimum $ map fst idx, maximum $ map fst idx)

    slice from to xs = take (to - from + 1) (drop from xs)

getGeneration arr' i
  | null arr' || i == 0 = arr'
  | otherwise = getGeneration (trim [[f' x y | x <- [0 .. col]] | y <- [0 .. row]]) (i - 1)
  where
    arr = padding arr'
    col = length (head arr) - 1
    row = length arr - 1
    f' x y
      | n == 3 || (v == 1 && n == 2) = 1
      | otherwise = 0
      where
        v = arr!!y!!x
        n = (-v) + sum [arr!!j!!i |
          i <- [max 0 (x-1) .. min col (x+1)],
          j <- [max 0 (y-1) .. min row (y+1)]]

    padding = transpose . map add . transpose . map add
      where
        add xs = [0] ++ xs ++ [0]

    trim = (!! 4) . iterate (rotate . until validHead tail)
      where
        validHead xs = null xs || (elem 1 . head $ xs)
        rotate = reverse . transpose
