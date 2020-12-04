module HighAndLow where

highAndLow1 :: String -> String
highAndLow1 xs = show (maximum ns) ++ " " ++ show (minimum ns)
  where
    ns = (map read $ words xs) :: [Int]

higAndLow2 :: String -> String
higAndLow2 = unwords . map show . sequence [maximum, minimum] . map (read :: String -> Int) . words
