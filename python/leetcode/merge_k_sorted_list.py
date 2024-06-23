from typing import List, Optional 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists( lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    def mergeSort(lists: List[Optional[ListNode]], start: int, end: int) -> ListNode:
        if start == end:
            return lists[start]
        
        mid = start + (end - start) // 2
        left = mergeSort(lists, start, mid)
        right = mergeSort(lists, mid+1, end)
        return merge(left, right)

    def merge(left: ListNode, right: ListNode) -> ListNode:
        begin = ListNode(None)
        temp = begin

        while left and right:
            if left.val < right.val:
                temp.next = left
                temp = left
                left = left.next 
            else:
                temp.next = right 
                temp = right 
                right = right.next

        remain = left if left else right 
        while remain:
            temp.next = remain
            temp = remain
            remain = remain.next

        while begin.val == None:
            begin = begin.next
        return begin

    if not lists:
        return None 
    return mergeSort(lists, 0, len(lists)-1)
