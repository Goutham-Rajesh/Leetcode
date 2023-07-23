# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=[]
        q.append(root)
        sum=root.val
        level=0
        final=1
        while(q):
            l=len(q)
            s=0
            for i in range(l):
                node=q.pop(0)
                if node:
                    s+=node.val
                    if(node.left!=None):
                        q.append(node.left)
                    if(node.right!=None):
                        q.append(node.right)
            level+=1
            if(s>sum):
                sum=s
                final=level
        return final
                
            
                
                
        
