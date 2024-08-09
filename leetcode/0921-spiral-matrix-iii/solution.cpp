class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart,
                                        int cStart) {
        vector<vector<int>> vis;
        int dir = 0; // 0 -> right, 1 -> down, 2 -> left, 3 -> up
        int x = rStart;
        int y = cStart;
        int steps = 1;
        int steps_i = 0;
        int step = 0;
        while (vis.size() < rows * cols) {
            if (x >= 0 && x < rows && y >= 0 && y < cols) {
                vector<int> v{x,y};
                vis.push_back(v);
            }
            //cout << x << " " << y << endl;
            //cout << step << "/" << steps << " " << steps_i << endl;
            //cout << vis.size() << endl;
            if (dir == 0) {
                ++y;
            } else if (dir == 1) {
                ++x;
            } else if (dir == 2) {
                --y;
            } else {
                --x;
            }
            ++step;
            if (step == steps) {
                ++dir;
                dir %= 4;
                step = 0;
                ++steps_i;
                if (steps_i == 2) {
                    steps_i = 0;
                    steps += 1;
                }
            }
        }
        return vis;
    }
};
