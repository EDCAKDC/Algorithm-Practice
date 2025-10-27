# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        cnt = Counter()

        def dfs(node):
            if not node:
                return 0
            s = dfs(node.left) + dfs(node.right) + node.val
            cnt[s] += 1
            return s
        dfs(root)
        mx = max(cnt.values())
        return [s for s, c in cnt.items() if c == mx]
