module UniqueInOrder (uniqueInOrder) where

import Data.List 

uniqueInOrder :: Eq a => [a] -> [a]
uniqueInOrder _list =  map head $ group _list