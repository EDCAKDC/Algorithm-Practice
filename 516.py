class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = 2+(dp[i+1][j-1] if j - i >=2 else 0)
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n-1,-1,-1):
            dp[i] = 1
            pre = 0
            for j in range(i+1,n):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = 2+pre
                else:
                    dp[j] = max(dp[j],dp[j-1])
                pre = tmp
        return dp[n-1]
