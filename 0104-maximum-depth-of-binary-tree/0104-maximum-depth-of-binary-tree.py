class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:  # Base case: if the node is None (empty subtree)
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            return max(left_depth, right_depth) + 1 # Add 1 for the current node

        return(dfs(root))
