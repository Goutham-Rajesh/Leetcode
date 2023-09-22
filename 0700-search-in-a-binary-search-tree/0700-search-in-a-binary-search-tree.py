# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        n=root
        while(n!=None):
            if(n.val>val):
                n=n.left
            elif(n.val<val):
                n=n.right
            elif(n.val==val):
                break
        return n
            
        
        