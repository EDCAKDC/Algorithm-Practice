class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0]*n for _ in range(n)]
        for length in range(3, n+1):
            for l in range(0, n-length+1):
                r = l + length - 1
                best = float('inf')
                for k in range(l+1, r):
                    best = min(best, dp[l][k]+dp[k][r] +
                               values[l]*values[k]*values[r])
                dp[l][r] = best
        return dp[0][n-1]
