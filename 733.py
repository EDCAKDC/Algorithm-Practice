class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        old = image[sr][sc]
        if old == color:
            return image

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return
            if image[i][j] != old:
                return
            image[i][j] = color
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        dfs(sr, sc)
        return image
