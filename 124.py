# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -2**32

        def dfs(u):
            if not u:
                return 0, -2**32
            left_best, left_down = dfs(u.left)
            right_best, right_down = dfs(u.right)
            sub_best = u.val + max(left_best, right_best, 0)
            best_through = u.val + max(left_best, 0) + max(right_best, 0)
            best = max(best_through, left_down, right_down)
            self.ans = max(self.ans, best)
            return sub_best, best
        dfs(root)
        return self.ans
