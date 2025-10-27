# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.best_val = root.val
        self.best_depth = -1
        def dfs(node,d):
            if not node:
                return None
            if d>self.best_depth:
                self.best_depth = d
                self.best_val = node.val
            dfs(node.left,d+1)
            dfs(node.right,d+1)
        
        dfs(root,0)
        return self.best_val