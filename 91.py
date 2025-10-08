class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        a, b = 1, 0
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                cur = 0
            else:
                cur = a
                if i+1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                    cur += b
            a, b = cur, a
        return a
