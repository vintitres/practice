class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = grid.copy()
        MAX = n * m * 200 + 1
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                res[i][j] += min(res[i - 1][j] if i > 0 else MAX, res[i][j - 1] if j > 0 else MAX)
        print(res)
        return res[n - 1][m - 1]

        
