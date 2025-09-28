from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        dir = (0, 1), (1, 0), (-1, 0), (0, -1)
        minutes = 0
        while q:
            size = len(q)
            processed = False
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dir:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
                        processed = True
            if processed:
                minutes += 1
        return minutes if fresh == 0 else -1
