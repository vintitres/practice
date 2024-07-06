class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int row_size = grid[0].size();
        vector<int> row = vector<int>(row_size);
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < row_size; ++j) {
                int x;
                if(j == 0) {
                    x = row[0];
                } else if (i == 0) {
                    x = row[j - 1];
                } else {
                    x = min(row[j], row[j - 1]);
                }
                row[j] = grid[i][j] + x;
            }
        }
        return row[row_size - 1];
    }
};
