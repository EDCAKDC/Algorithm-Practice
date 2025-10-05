import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v, w))
        inf = 2**32 - 1
        dist = [inf]*(n+1)
        dist[k] = 0
        heap = [(0, k)]
        visited = [False] * (n+1)

        while heap:
            d, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True

            for v, w in g[u]:
                if not visited[v] and d+w < dist[v]:
                    dist[v] = d+w
                    heapq.heappush(heap, (dist[v], v))

        ans = max(dist[1:])
        return -1 if ans >= inf else ans
