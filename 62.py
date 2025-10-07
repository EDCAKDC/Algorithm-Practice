class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        for c in range(m):
            dp[c][0] = 1
        for d in range(n):
            dp[0][d] = 1
        for c in range(1, m):
            for d in range(1, n):
                dp[c][d] = dp[c-1][d] + dp[c][d-1]
        return dp[m-1][n-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for c in range(1, m):
            for d in range(1, n):
                dp[d] += dp[d-1]

        return dp[-1]
