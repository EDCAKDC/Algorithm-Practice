from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
        dist = [[0]*n for _ in range(m)]
        inf = 10**9
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    dist[i][j] = inf
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr,nc))
        return dist
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
        inf = 10**9
        dist = [[inf]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m-1:
                    dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                if j < n -1:
                    dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
        return dist
        