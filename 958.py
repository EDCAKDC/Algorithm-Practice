# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, True, 0

            lc, lp, lh = dfs(node.left)
            rc, rp, rh = dfs(node.right)

            is_perfect = lp and rp and (lh == rh)

            case1 = lp and rc and (lh == rh)
            case2 = lc and rp and (lh == rh + 1)
            is_complete = lc and rc and (case1 or case2)

            return is_complete, is_perfect, max(lh, rh) + 1

        is_complete, _, _ = dfs(root)
        return is_complete
