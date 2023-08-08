# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        m=0
        fast,slow=head,head
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
        prev=None
        while(slow):
            n=slow.next
            slow.next=prev
            prev=slow
            slow=n
        start=head
        while(prev):
            m=max(m,start.val+prev.val)
            start=start.next
            prev=prev.next
        return m
            
            
        
            
        