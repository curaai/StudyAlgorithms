from typing import List, Tuple

def first_solution(height: List[int]) -> int:
    def find_traps() -> List[Tuple[int, int]]:
        if not height: return []

        res = []
        left = 0
        length = len(height)

        while (left + 1) < length:
            if height[left] < height[left+1]:
                left += 1
                continue 

            targets = []
            for i in range(left+2, length):
                if height[left] <= height[i]:
                    targets.append(i)
                    break
                elif height[left + 1] < height[i]:
                    targets.append(i)

            right = max(targets, key=lambda i: height[i], default=None)

            if right is not None and right - left >= 2:
                res.append((left, right))
                left = right - 1
                
            left += 1 
        return res

    def amount_of_trap(trap):
        left, right = trap
        _min = min(height[left], height[right])

        return sum(map(lambda x: _min - x, height[left+1:right]))

    return sum(map(amount_of_trap, find_traps()))

def trap(height: List[int]) -> int:
    if len(height) <= 2: return 0

    max_l, max_r = height[0], height[-1]
    l, r = 1, len(height) - 2

    res = 0
    while l <= r:
        if max_l < max_r:
            if max_l < height[l]:
                max_l = height[l]
            else:
                res += max_l - height[l]
            l += 1
        else:
            if max_r < height[r]:
                max_r = height[r]
            else:
                res += max_r - height[r]
            r -= 1
    return res

a = \
    [0,1,0,2,1,0,1,3,2,1,2,1]
    # [4,2,0,3,2,5]

print(trap(a))