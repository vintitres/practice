class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int row_below[n];
        row_below[n - 1] = grid[m - 1][n - 1];
        for (int j = n - 2; j >= 0; --j) {
            row_below[j] = grid[m - 1][j] + row_below[j + 1];
        }
        for (int i = m - 2; i >= 0; --i) {
            row_below[n - 1] = grid[i][n - 1] + row_below[n - 1];
            for (int j = n - 2; j >= 0; --j) {
                row_below[j] = grid[i][j] + min(row_below[j], row_below[j + 1]);
            }
        }
        return row_below[0];
    }
};
