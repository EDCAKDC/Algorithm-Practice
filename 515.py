# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []    
        queue = deque([root])
        while queue:
            maxval = float('-inf')
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                maxval = max(maxval,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(maxval)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node,depth):
            if not node:
                return 
            if depth == len(res):
                res.append(node.val)
            else:
                res[depth] = max(res[depth],node.val)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return res