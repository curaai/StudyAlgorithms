# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
# Maximum subarray sum
# solve with kadane algorithm

def max_sequence(arr):
    global_, local_ = 0, 0
    for x in arr:
        local_ = max(x, x + local_)
        if global_ < local_:
            global_ = local_

    return global_