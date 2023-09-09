# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        c=0
        def dfs1(root,s):
            nonlocal c
            if not root:
                return
            dfs1(root.left,s+root.val)
            dfs1(root.right,s+root.val)
            if(s+root.val==targetSum):
                c+=1
        def dfs(root):
            if not root:
                return
            dfs1(root,0)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return c
            
        
           
        
        

            
                
