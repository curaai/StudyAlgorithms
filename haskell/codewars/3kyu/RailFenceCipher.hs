import Data.List (sortOn)

{- First Answer
encode :: [a] -> Int -> [a]
encode xs rail = concat [map snd . filter ((==n) . fst) $ xs' | n <- [0 .. rail-1]]
where
xs' = zip (idxGenerator rail) xs

decode xs railCnt = map char [0 .. length xs - 1]
  where
    char i = let j = idx!!i in rails!!j!!(length . filter (== j) . take i ) idx
    idx = take (length xs) (idxGenerator railCnt)
    rails = [rail n | n <- [0 .. railCnt -1]]
    rail i = take take' . drop drop' $ xs
      where 
        drop' = length . filter (<i) $ idx
        take' = length . filter (==i) $ idx

idxGenerator n = cycle $ xs ++ (init . tail . reverse) xs
  where xs = [ 0 .. n-1]
-}

encode :: [a] -> Int -> [a]
encode str n = map snd . sortOn fst $ zip (cycle ([1..n] ++ [n-1,n-2..2])) str

decode str n = map snd . sortOn snd $ zip (encode [1..length str] n) str