# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=[]
        q.append(root)
        result=[]
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                if(node):
                    if(node.left):
                        q.append(node.left)
                    if(node.right):
                        q.append(node.right)
            if(node):
                result.append(node.val)

        return result
        