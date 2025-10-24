# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        prev_val = None   
        count = 0
        max_count = 0
        modes = []

        def touch(x):
            nonlocal prev_val, count, max_count, modes
            if prev_val is None or x != prev_val:
                prev_val = x
                count = 1
            else:
                count += 1
            if count > max_count:
                max_count = count
                modes = [x]
            elif count == max_count:
                modes.append(x)

        cur = root
        while cur:
            if cur.left is None:
                touch(cur.val)
                cur = cur.right
            else:
                pred = cur.left
                while pred.right and pred.right is not cur:
                    pred = pred.right
                if pred.right is None:
                    pred.right = cur
                    cur = cur.left
                else:
                    pred.right = None
                    touch(cur.val)
                    cur = cur.right

        return modes
