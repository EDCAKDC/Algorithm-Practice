# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def lh(x):
            h = 0
            while x:
                h += 1
                x = x.left
            return h

        def rh(x):
            h = 0
            while x:
                h += 1
                x = x.right
            return h

        def solve(node):
            if not node:
                return 0
            left_height = lh(node)
            right_height = rh(node)
            if left_height == right_height:
                return (1 << left_height) - 1
            return 1 + solve(node.left) + solve(node.right)
        return solve(root)
