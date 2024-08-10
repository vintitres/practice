const char SIDES[] = {'l', 'r', 'u', 'd'};
typedef vector<vector<short>> VisSet;


class Solution {
    short smask(char side) {
        if (side == 'l') {
            return 1;
        } else if (side == 'r') {
            return 1<<1;
        } else if (side == 'u') {
            return 1<<2;
        } else if (side == 'd') {
            return 1<<3;
        }
        assert(false);
        return 0;
    }
    bool contains(VisSet const& vis, tuple<int,int,char> const& xys) {
        auto [x,y,side] = xys;
        return vis[x][y] & smask(side);
    }
    void insert(VisSet & vis, tuple<int,int,char> const& xys) {
        auto [x,y,side] = xys;
        vis[x][y] |= smask(side);
    }
    void fill_area(int x, int y, char side, vector<string> const& grid,
                   VisSet& vis) {
        queue<tuple<int, int, char>> q;
        q.push({x,y,side});
        auto qadd = [&](tuple<int, int, char> el) {
            auto [x, y, s] = el;
            if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size()) {
                return;
            }
            if (!contains(vis, el)) {
                q.push(el);
            }
        };
            
        while (!q.empty()) {
            auto xys = q.front();
            q.pop();
            if (contains(vis, xys)) {
                continue;
            }
            auto [x, y, side] = xys;
            if (grid[x][y] == ' ') {
                for (char side : SIDES) {
                    insert(vis, {x, y, side});
                }
                qadd({x + 1, y, 'u'});
                qadd({x - 1, y, 'd'});
                qadd({x, y + 1, 'l'});
                qadd({x, y - 1, 'r'});
            } else if (grid[x][y] == '/') {
                if (side == 'l' || side == 'u') {
                    insert(vis, {x, y, 'l'});
                    insert(vis, {x, y, 'u'});
                    qadd({x - 1, y, 'd'});
                    qadd({x, y - 1, 'r'});
                } else {
                    insert(vis, {x, y, 'r'});
                    insert(vis, {x, y, 'd'});
                    qadd({x + 1, y, 'u'});
                    qadd({x, y + 1, 'l'});
                }
            } else { // "\"
                if (side == 'l' || side == 'd') {
                    insert(vis, {x, y, 'l'});
                    insert(vis, {x, y, 'd'});
                    qadd({x + 1, y, 'u'});
                    qadd({x, y - 1, 'r'});
                } else {
                    insert(vis, {x, y, 'r'});
                    insert(vis, {x, y, 'u'});
                    qadd({x, y + 1, 'l'});
                    qadd({x - 1, y, 'd'});
                }
            }
        }
    }

    void print(vector<string> const& grid) {
        for (int x = 0; x < grid.size(); ++x) {
            cout << grid[x] << endl;
        }
        cout << endl;
    }

public:
    int regionsBySlashes(vector<string>& grid) {
        //print(grid);
        int count_areas = 0;
        VisSet vis(grid.size(), vector<short>(grid[0].size(), 0));
        for (int x = 0; x < grid.size(); ++x) {
            for (int y = 0; y < grid[0].size(); ++y) {
                for (char side : SIDES) {
                    if (!contains(vis, {x, y, side})) {
                        ++count_areas;
                        //cout << "!" << endl;
                        fill_area(x, y, side, grid, vis);
                    }
                }
            }
        }
        return count_areas;
    }
};
