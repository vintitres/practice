#define MOD 1000000007
class Solution {
    bool in(int m, int n, int x, int y) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }
public:
    int paths(const int m, const int n, int maxMove, int x, int y, map<tuple<int,int,int>,int>& paths_mem) {
        if (!in(m, n, x, y)) {
            return 1;
        }
        if (maxMove == 0) {
            return 0;
        }
        auto paths_mem_index = make_tuple(maxMove, x, y);
        auto it = paths_mem.find(paths_mem_index);
        if (it != paths_mem.end()) {
            return it->second;
        }
        int ret = 0;
        ret += paths(m, n, maxMove - 1, x + 1, y, paths_mem);
        ret %= MOD;
        ret += paths(m, n, maxMove - 1, x - 1, y, paths_mem);
        ret %= MOD;
        ret += paths(m, n, maxMove - 1, x, y + 1, paths_mem);
        ret %= MOD;
        ret += paths(m, n, maxMove - 1, x, y - 1, paths_mem);
        ret %= MOD;
        paths_mem[paths_mem_index] = ret;
        return ret;
    }
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        map<tuple<int,int,int>,int> paths_mem;
        return paths(m, n, maxMove, startRow, startColumn, paths_mem);
    }
};
