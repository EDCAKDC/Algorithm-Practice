# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional


class Solution:
    def generateTrees(self, n: int) -> List[Optional['TreeNode']]:
        if n == 0:
            return []

        dp = [[None] * (n + 2) for _ in range(n + 2)]

        def get(lo: int, hi: int):

            if lo > hi:
                return [None]
            return dp[lo][hi]

        for length in range(1, n + 1):
            for lo in range(1, n - length + 2):
                hi = lo + length - 1
                res = []

                for root in range(lo, hi + 1):
                    left_list = get(lo, root - 1)
                    right_list = get(root + 1, hi)
                    for L in left_list:
                        for R in right_list:
                            node = TreeNode(root)
                            node.left = L
                            node.right = R
                            res.append(node)
                dp[lo][hi] = res

        return dp[1][n]
