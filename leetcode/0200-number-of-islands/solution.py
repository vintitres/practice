class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == "1":
                    islands += 1
                    seen.add((i,j))
                    q = deque([(i, j)])
                    while q:
                        ii, jj = q.popleft()
                        for iii, jjj in [(ii + 1, jj), (ii - 1, jj), (ii, jj + 1), (ii, jj - 1)]:
                            if (iii, jjj) not in seen and iii >= 0 and iii < len(grid) and jjj >= 0 and jjj < len(grid[0]) and grid[iii][jjj] == "1":
                                seen.add((iii, jjj))
                                q.append((iii, jjj))
                        

        return islands
        
