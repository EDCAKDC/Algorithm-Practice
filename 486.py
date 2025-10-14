class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
            for length in range(2, n+1):
                for i in range(0, n - length + 1):
                    j = i + length - 1
                    dp[i][j] = max(nums[i]-dp[i+1][j], nums[j] - dp[i][j-1])
            return dp[0][n-1] >= 0


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]
        for i in range(n-2, -1, -1):
            dp[i] = nums[i]
            for j in range(i+1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
        return dp[n-1] >= 0
