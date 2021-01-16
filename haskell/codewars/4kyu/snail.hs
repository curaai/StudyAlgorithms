module Snail where

import Data.List ( transpose )

snail :: [[Int]] -> [Int]
snail [] = []
snail (xs:xss) = xs ++ (snail . reverse . transpose) xss
