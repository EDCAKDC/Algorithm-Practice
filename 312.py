from functools import lru_cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        vals = [1]+nums+[1]
        m = len(vals)

        @lru_cache(None)
        def solve(l, r):
            if r-l <= 1:
                return 0
            best = 0
            for k in range(l+1, r):
                best = max(best, solve(l, k)+solve(k, r) +
                           vals[l]*vals[k]*vals[r])
            return best
        return solve(0, m-1)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        vals = [1]+nums+[1]
        m = len(vals)
        dp = [[0]*m for _ in range(m)]
        for length in range(3, m+1):
            for l in range(0, m-length+1):
                r = l + length - 1
                best = 0
                for k in range(l+1, r):
                    best = max(best, dp[l][k]+dp[k][r]+vals[l]*vals[k]*vals[r])
                dp[l][r] = best
        return dp[0][m-1]
