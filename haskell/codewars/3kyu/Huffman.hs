module Huffman
    ( frequencies
    , encode
    , decode
    , Bit (..)
    ) where

import Data.List

data Bit = Z | O deriving (Eq, Show)

test = "aaaabbc"

{-| 
>>> frequencies test
[('a',4),('b',2),('c',1)]

>>> target [('a',4),('b',2),('c',1)] 
[('a',4)]
-}

-- | Calculate symbol frequencies of a text.
frequencies :: Ord a => [a] -> [(a, Int)]
frequencies xs = sortBy (flip sortSnd) $ zip unique (map count unique)
    where
        sortSnd (_,a) (_,b) = compare a b
        unique = nub xs
        count x = length . filter (==x) $ xs

-- | Encode a sequence using the given frequencies.
encode :: Ord a => [(a, Int)] -> [a] -> Maybe [Bit]
encode freq lens = error "encode not yet implemented"
    where 
        target = filter (\x -> fst x `elem` lens)
        -- serialize x:xs = map ( ++ [O]) xs
        serialize xs = [[O]] -- [x ++ [Z]] ++ map (serialize . (\x -> x++[O])) xs
            where
                x = head xs:O

-- | Decode a bit sequence using the given frequencies.
decode :: [(a, Int)] -> [Bit] -> Maybe [a]
decode = error "decode not yet implemented"
