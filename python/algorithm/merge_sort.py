import unittest
from typing import List

def merge(left: List[int], right: List[int]) -> List[int]:
    '''
    [0, 3], [1, 2]
    - `i` is enumerate index of left 
    - `j` is enumerate index of right 
    - l = left[i]
    - r = right[i]

    1.  until iterate all elements of two 
    2. l < r 
    then insert l
    else insert r 
    2#. [0, 3], [1, 2]
    -> {0}, [3], [1,2]
    -> {0, 1}, [3], [2]
    -> {0, 1, 2}, [3], []
    3. repeat until left one element in either left or right
    4. append left to res
    '''

    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        l = left[i]
        r = right[j]
        if l < r:
            res.append(l)
            i += 1
        else:
            res.append(r)
            j += 1
    res += left[i:]
    res += right[j:]
    return res


def sort(arr: List[int]) -> List[int]:
    if len(arr) > 1:
        mid = len(arr) // 2 
        left = arr[:mid]
        right = arr[mid:]

        l = sort(left)
        r = sort(right)
        return merge(l, r)
    else:
        return arr 



class TestMergeSort(unittest.TestCase):

    def test_merge(self):
        v = [0, 3], [1, 2]
        res = merge(*v)
        self.assertEqual([0, 1, 2, 3], res)

    def test_sort(self):
        v = [3, 5, 1, 4, 2, 6]
        res = sort(v)
        self.assertEqual(list(range(1, 7)), res)


if __name__ == "__main__":
    unittest.main()
     