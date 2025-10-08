class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        n = len(s)
        if not s:
            return True
        lmax = max(map(len, wordset)) if wordset else 0
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(max(0, i-lmax), i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        return dp[n]
