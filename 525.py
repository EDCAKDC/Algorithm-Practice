class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        first = {0:-1}
        best = 0
        for i, x in enumerate(nums):
            count += 1 if x==1 else -1
            if count in first:
                best = max(best, i - first[count])
            else:
                first[count] = i
        return best