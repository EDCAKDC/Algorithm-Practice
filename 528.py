import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        idx = bisect.bisect_left(self.prefix,x)
        return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()