from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        all = (1 << n) - 1
        q = deque()
        visited = [[False]*(1 << n) for _ in range(n)]
        for i in range(n):
            mask = 1 << i
            q.append((i, mask, 0))
            visited[i][mask] = True

        while q:
            u, mask, dist = q.popleft()
            if mask == all:
                return dist
            for v in graph[u]:
                new = mask | (1 << v)
                if not visited[v][new]:
                    visited[v][new] = True
                    q.append((v, new, dist+1))
        return -1
