from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        cnt = Counter(nums)

        if k == 0:
            return sum(1 for v in cnt.values() if v >= 2)

        ans = 0
        for x in cnt:
            if x + k in cnt:
                ans += 1
        return ans
