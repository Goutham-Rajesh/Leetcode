# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def postorder(root):
            if(root):
                if(root.left):
                    postorder(root.left)
                if(root.right):
                    postorder(root.right)
                if(root.left==None and root.right==None):
                    a.append(root.val)
            return a
        a=[]
        x=postorder(root1)
        a=[]
        y=postorder(root2)
        if(x==y):
            return True
        