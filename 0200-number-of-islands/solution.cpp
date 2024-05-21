class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> vis(m);
        for (int i = 0; i < m; ++i) {
            vis[i].resize(n, false);
        } 
        int isl = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (vis[i][j]) {
                    continue;
                }
                if (grid[i][j] == '1') {
                    ++isl;
                    queue<pair<int,int>> island;
                    island.push(make_pair(i, j));
                    while (!island.empty()) {
                        int i, j;
                        tie(i, j) = island.front();
                        island.pop();
                        if (i < 0 || i >= m || j < 0 || j >= n || vis[i][j] || grid[i][j] == '0') continue;
                        vis[i][j] = 1;
                        for (auto neigh : {make_pair(i + 1, j), make_pair(i - 1, j), make_pair(i, j + 1), make_pair(i, j - 1)}) {
                            island.push(neigh);
                        }
                    }
                }
            }
        }
        return isl;
    }
};
