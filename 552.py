class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0]*3 for _ in range(2)]
        dp[0][0] = 1
        for _ in range(n):
            new = [[0]*3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    cur = dp[a][l]
                    if cur == 0:
                        continue
                    new[a][0] = (new[a][0] + cur) % MOD
                    if a == 0:
                        new[1][0] = (new[1][0] + cur) % MOD
                    if l < 2:
                        new[a][l+1] = (new[a][l+1] + cur) % MOD
            dp = new
        ans = 0
        for a in range(2):
            for l in range(3):
                ans = (ans + dp[a][l]) % MOD
        return ans
