class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r,c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        def dfs(x,y):
            if not (0 <= x < m and 0 <=y < n) or board[x][y] != 'E':
                return
            mines = 0
            for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                nx,ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                    mines += 1
            if mines > 0:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                    dfs(x+dx,y+dy) 
        dfs(r, c)
        return board