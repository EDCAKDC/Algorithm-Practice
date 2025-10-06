class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n

        def f(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(f(i-1), nums[i]+f(i-2))
            return dp[i]
        return f(n-1)
