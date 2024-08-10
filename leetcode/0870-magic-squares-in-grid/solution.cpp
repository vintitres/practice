class Solution {
public:
    int isMagicSquare(vector<vector<int>> const& grid, int xx, int yy) {
        vector<bool> digits(10, 0);
        int exp_sum = 0;
        //cout << xx << " " << yy << endl;
        for (int y = yy; y < yy + 3; ++y) {
            //cout << y << endl;
            exp_sum += grid[xx][y];
        }
        for (int x = xx; x < xx + 3; ++x) {
            int sum = 0;
            for (int y = yy; y < yy + 3; ++y) {
                if (grid[x][y] <= 9) {
                    digits[grid[x][y]] = true;
                }
                sum += grid[x][y];
            }
            if (sum != exp_sum) {
                return false;
            }
        }
        for (int i = 1; i <= 9; ++i) {
            if (!digits[i]) {
                return false;
            }
        }
        for (int y = yy; y < yy + 3; ++y) {
            int sum = 0;
            for (int x = xx; x < xx + 3; ++x) {
                sum += grid[x][y];
            }
            if (sum != exp_sum) {
                return false;
            }
        }
        int sum = 0;
        for (int y = yy, x = xx; y < yy + 3; ++y) {
            sum += grid[x][y];
            ++x;
        }
        if (sum != exp_sum) {
            return false;
        }
        sum = 0;
        for (int y = yy, x = xx + 2; y < yy + 3; ++y) {
            sum += grid[x][y];
            --x;
        }
        if (sum != exp_sum) {
            return false;
        }


        return true;
    }
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int cnt = 0;
        if (grid.size() < 3 || grid[0].size() < 3) {
            return 0;
        }
        for (int i = 0; i < grid.size() - 2; ++i) {
            for (int j = 0; j < grid[0].size() - 2; ++j) {
                if (isMagicSquare(grid, i, j)) {
                    ++cnt;
                }
            }
        }
        return cnt;
        
    }
};
