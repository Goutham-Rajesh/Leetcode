# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def post(self,root: TreeNode,m: int) -> int:
        c=0
        if(root):
            if(root.val>=m):
                c+=1
                m=root.val
            return c+self.post(root.left,m)+self.post(root.right,m)
        else:
            return 0

    def goodNodes(self, root: TreeNode) -> int:
        m=root.val
        c=self.post(root,m)
        return c


        
        
        