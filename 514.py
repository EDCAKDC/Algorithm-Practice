from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        pos = defaultdict(list)
        for i,ch in enumerate(ring):
            pos[ch].append(i)
        nxt_dp = [0]*n
        inf = 10**9
        for ch in reversed(key):
            cur_dp = [inf]*n
            targets = pos[ch]
            for j in range(n):
                best = inf
                for k in targets:
                    diff = abs(j-k)
                    rot = min(diff,n-diff)
                    best = min(best,rot + 1 + nxt_dp[k])
                cur_dp[j] = best
            nxt_dp = cur_dp
        return nxt_dp[0]