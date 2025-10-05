import heapq
from collections import defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            g[u].append((v, p))
            g[v].append((u, p))
        prob = [0.0]*n
        prob[start_node] = 1.0
        heap = [(-1.0, start_node)]
        while heap:
            negp, u = heapq.heappop(heap)
            p = -negp
            if u == end_node:
                return p
            if p < prob[u]:
                continue
            for v, w in g[u]:
                nd = p*w
                if nd > prob[v]:
                    prob[v] = nd
                    heapq.heappush(heap, (-nd, v))
        return 0.0
