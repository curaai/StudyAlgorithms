import unittest
from functools import reduce
from collections import Counter


def common(a:list, b:list, c:list) -> int:
    def intersect(fst:Counter, snd:Counter) -> Counter:
        def get_min_val(k):
            x, y = fst[k], snd[k]
            return (k, x if x < y else y)

        inter_keys = set(fst.keys()).intersection(set(snd.keys()))
        return Counter(dict(map(get_min_val, inter_keys)))

    def calc(c: Counter) -> int:
        return sum(map(lambda k: k* c[k], c.keys()))

    return calc(reduce(intersect, map(Counter, [a, b, c])))


class TestCommonElement(unittest.TestCase):
    
    def test_only_three_elements(self):
        input_ = [1,2,3],[5,3,2],[7,3,2]
        self.assertEqual(common(*input_), 5)

    def test_only_four_elements(self):
        input_ = ([1,2,2,3],[5,3,2,2],[7,3,2,2])
        self.assertEqual(common(*input_), 7)


if __name__ == '__main__':
    unittest.main()