class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]
        for i in range(n-2, -1, -1):
            dp[i] = piles[i]
            for j in range(i+1, n):
                dp[j] = max(piles[i]-dp[j], piles[j]-dp[j-1])
        return dp[n-1] > 0


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
