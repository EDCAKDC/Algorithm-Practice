# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(u):
            if not u:
                return 0, 0
            lt, ls = dfs(u.left)
            rt, rs = dfs(u.right)
            take = u.val + ls + rs
            skip = max(lt, ls) + max(rt, rs)
            return take, skip
        return max(dfs(root))
