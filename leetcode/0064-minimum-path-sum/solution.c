#define MIN(x, y) (x < y ? x : y)

int minPathSum(int** grid, int gridRowSize, int *gridColSizes) {
    int n = gridColSizes[0], p[n], i, j;
    p[0] = 0;
    for (i = 0; i < gridRowSize; ++i) {
        p[0] = grid[i][0] + p[0];
        for (j = 1; j < n; ++j) {
            if (i == 0) {
                p[j] = grid[i][j] + p[j - 1];
            } else {
                p[j] = grid[i][j] + MIN(p[j - 1], p[j]);
            }
        }
    }
    return p[n - 1];
        
}
