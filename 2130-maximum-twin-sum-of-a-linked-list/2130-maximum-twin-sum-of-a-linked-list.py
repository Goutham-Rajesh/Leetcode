# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l=[]
        m=0
        temp=head
        while(temp):
            l.append(temp.val)
            temp=temp.next
        for i in range(len(l)//2):
            m=max(m,l[i]+l[len(l)-i-1])
        return m
            
            
        