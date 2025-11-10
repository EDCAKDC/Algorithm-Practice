class Solution:
    def countArrangement(self, n: int) -> int:
        options = [[] for _ in range(n+1)]
        for pos in range(1, n+1):
            for num in range(1, n+1):
                if pos % num == 0 or num % pos == 0:
                    options[pos].append(num)
        used = [False] * (n+1)
        ans = 0
        order = list(range(1, n+1))
        order.sort(key=lambda p: len(options[p]))

        def dfs(k):
            nonlocal ans
            if k == n:
                ans += 1
                return
            pos = order[k]
            for num in options[pos]:
                if not used[num]:
                    used[num] = True
                    dfs(k+1)
                    used[num] = False
        dfs(0)
        return ans
from functools import lru_cache
class Solution:
    def countArrangement(self, n: int) -> int:
        options = [[] for _ in range(n+1)]
        for pos in range(1, n+1):
            for num in range(1, n+1):
                if pos % num == 0 or num % pos == 0:
                    options[pos].append(num)
        order = list(range(1, n+1))
        order.sort(key=lambda p: len(options[p]))
        @lru_cache(maxsize=None)
        def dp(mask):
            k = mask.bit_count()
            if k == n:
                return 1
            pos = order[k]
            total = 0
            for num in options[pos]:
                bit = 1<<(num-1)
                if not (mask&bit):
                    total += dp(mask | bit)
            return total
        return dp(0)

    