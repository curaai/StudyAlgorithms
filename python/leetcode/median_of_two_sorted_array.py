def two_pointer_method(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    j=0; i=0; a=0; b=0

    for moveCount in range(int((n + m) / 2) + 1):
        a = b
        if(i != n and j != m and nums1[i] <= nums2[j]):
            b = nums1[i]
            i += 1
        elif(j < m):
            b = nums2[j]
            j += 1
        else:
            b = nums1[i]
            i += 1

    if((n+m) % 2 == 0):
        return (a + b) / 2
    else:
        return b
