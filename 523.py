class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if k == 0:
            for i in range(n-1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False
        k = abs(k)
        prefix = 0
        first = {0:-1}
        for i,x in enumerate(nums):
            prefix += x
            r = prefix%k
            if r in first:
                if i - first[r] >= 2:
                    return True
            else:
                first[r] = i
        return False
