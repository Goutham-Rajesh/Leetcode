# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=[]
        if(head==None):
            return False
        if(head.next==None):
            return False
        s=head
        f=head.next.next
        while(f):
            if(f==s):
                return True
            if(f.next):
                s=s.next
                f=f.next.next
            else:
                break
        return False
            
        
        