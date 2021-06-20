-- stack script --resolver lts-17.14 --package HUnit
module NextSmaller where

import Data.List
import Data.Maybe
import Data.Ord ( Down(Down) )

import Test.HUnit

nextSmaller :: Integer -> Maybe Integer
nextSmaller n
  | isMaxCase n = Nothing
  | otherwise = do
    invalidIdx <- findInvalidIndex xs'
    let swapIdx = findLargestIndex (xs'!!invalidIdx) ( drop (invalidIdx + 1) xs' )
        xs'' = swapElementsAt invalidIdx (invalidIdx + 1 + swapIdx) xs'
    return . read $  take (invalidIdx+1) xs'' ++ (reverse . sort . drop (invalidIdx+1)) xs''
    where
      xs' = show n

isMaxCase n = sn == res
  where
    sn = show n
    res =
      let xs = sort sn
       in if head xs == '0'
            then xs !! 1 : xs !! 0 : drop 2 xs
            else xs

findInvalidIndex :: Ord a => [a] -> Maybe Int
findInvalidIndex xs
  | null invalids = Nothing
  | otherwise = Just . fst . head $ invalids
  where
    invalids = dropWhile (uncurry (<=) . snd) $ reverse $ zip [0 ..] (zip (init xs) (tail xs))

findLargestIndex :: (Ord b, Num c, Enum c) => b -> [b] -> c
findLargestIndex x xs = fst . head . dropWhile (\(i, y )-> x <= y) $ sortOn (Down . snd) (zip [0..] xs)

swapElementsAt :: Int -> Int -> [a] -> [a]
swapElementsAt i j xs = let elemI = xs !! i
                            elemJ = xs !! j
                            left = take i xs
                            middle = take (j - i - 1) (drop (i + 1) xs)
                            right = drop (j + 1) xs
                    in  left ++ [elemJ] ++ middle ++ [elemI] ++ right

test1 = TestCase $ assertEqual "1" (Just 1) (findInvalidIndex "531")
test2 = TestCase $ assertEqual "2" (Just 144) (nextSmaller 414)
test3 = TestCase $ assertEqual "3" (Just 0) (findInvalidIndex "414")
test4 = TestCase $ assertEqual "4" Nothing (nextSmaller 1027)
test5 = TestCase $ assertEqual "5" (Just 123456789) (nextSmaller 123456798)
test6 = TestCase $ assertEqual "6" Nothing (nextSmaller 123456789)
test7 = TestCase $ assertEqual "7" (Just 1234567890) (nextSmaller 1234567908)
test8 = TestCase $ assertEqual "8" (Just 66744) (nextSmaller 67446)

main = runTestTT $ TestList[test1, test2, test3, test4, test5, test6, test7, test8]
