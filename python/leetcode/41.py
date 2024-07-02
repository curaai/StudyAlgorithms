from typing import List
import itertools

def firstMissingPositive(nums: List[int]) -> int:
    nums = set(nums)
    return next(filter(lambda i: i not in nums, itertools.count(start=1)))