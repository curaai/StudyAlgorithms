from typing import List

class Solution:
    def first_solution(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []

        word_len = len(words[0])
        _range = list(range(len(words)))
        cache = dict()

        def f(i: int, s: str):
            seen = set()

            find = lambda iw:s[i:].startswith(words[iw])
            while True: 
                if i in cache:
                    seen.add(cache[i])
                    i += word_len
                    continue

                unseen_words = filter(lambda j: j not in seen, _range)
                iw = next(filter(find, unseen_words), None)
                if iw is not None:
                    seen.add(iw)
                    cache[i] = iw
                    i += word_len
                else:
                    return len(seen) == len(words)
        
        res = []
        i = 0
        total_length = word_len * len(words)
        limit = len(s) - total_length
        while i <= limit:
            valid = f(i, s)
            if valid:
                res.append(i)
            i += 1

        return res
