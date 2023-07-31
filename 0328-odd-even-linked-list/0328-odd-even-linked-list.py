# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        o=head
        if(head==None):
            return None
        if(head.next==None):
            return head
        eh=head.next
        e=head.next
        while(e and e.next):
            o.next=e.next
            o=o.next
            e.next=o.next
            e=e.next
        o.next=eh
        return head
        