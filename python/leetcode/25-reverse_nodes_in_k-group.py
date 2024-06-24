from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr: return head 
            curr = curr.next 

        bck = None
        curr = head
        for _ in range(k):
            fwd = curr.next
            curr.next = bck
            bck = curr
            curr = fwd

        head.next = self.reverseKGroup(curr, k)
        return bck
        