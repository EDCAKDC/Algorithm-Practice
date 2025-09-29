from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m = len(heights)
        n = len(heights[0])

        def bfs(starts):
            q = deque(starts)
            visited = set(starts)
            dir = (0, 1), (1, 0), (-1, 0), (0, -1)
            while q:
                r, c = q.popleft()
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return visited

        pac_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atl_starts = [(m-1, c) for c in range(n)] + [(r, n - 1)
                                                     for r in range(m)]

        pac = bfs(pac_starts)
        atl = bfs(atl_starts)
        return [[r, c] for (r, c) in pac & atl]


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m = len(heights)
        n = len(heights[0])
        dir = ((0, 1), (1, 0), (-1, 0), (0, -1))
        pac = set()
        atl = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                    dfs(nr, nc, visited)

        for c in range(n):
            dfs(0, c, pac)
        for r in range(m):
            dfs(r, 0, pac)
        for c in range(n):
            dfs(m-1, c, atl)
        for r in range(m):
            dfs(r, n-1, atl)
        return [[r, c] for (r, c) in pac & atl]
