import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        inf = 2**32-1
        dist = [[inf]*n for _ in range(n)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while heap:
            d, x, y = heapq.heappop(heap)
            if (x, y) == (m-1, n-1):
                return d
            if d > dist[x][y]:
                continue
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n:
                    w = abs(heights[nx][ny] - heights[x][y])
                    nd = max(d, w)
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heapq.heappush(heap, (nd, nx, ny))
