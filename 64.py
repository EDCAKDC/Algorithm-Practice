class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for c in range(1, m):
            dp[c][0] = dp[c-1][0] + grid[c][0]
        for d in range(1, n):
            dp[0][d] = dp[0][d-1] + grid[0][d]
        for c in range(1, m):
            for d in range(1, n):
                dp[c][d] = min(dp[c-1][d], dp[c][d-1]) + grid[c][d]
        return dp[m-1][n-1]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        inf = 2**32-1
        dp = [inf]*n
        dp[0] = 0
        for c in range(m):
            dp[0] += grid[c][0]
            for d in range(1, n):
                dp[d] = grid[c][d] + min(dp[d], dp[d-1])
        return dp[-1]
