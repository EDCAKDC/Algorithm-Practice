import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        project = sorted(zip(capital,profits))
        maxheap = []
        i = 0
        for _ in range(k):
            while i < len(project) and w>=project[i][0]:
                heapq.heappush(maxheap,-project[i][1])
                i += 1
            if not maxheap:
                break
            w += -heapq.heappop(maxheap)
        return w
        