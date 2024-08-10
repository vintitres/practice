const char SIDES[] = {'l', 'r', 'u', 'd'};
typedef set<tuple<int, int, char>> VisSet;  // could be 3 dim array of bools (grid.size() x grid[0].size() x 4)

class Solution {
    void fill_area(int x, int y, char side, vector<string> const& grid,
                   VisSet& vis) {
        queue<tuple<int, int, char>> q;
        q.push({x,y,side});
        auto qadd = [&](tuple<int, int, char> el) {
            auto [x, y, s] = el;
            if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size()) {
                return;
            }
            if (!vis.contains(el)) {
                q.push(el);
            }
        };
            
        while (!q.empty()) {
            auto xys = q.front();
            q.pop();
            if (vis.contains(xys)) {
                continue;
            }
            auto [x, y, side] = xys;
            if (grid[x][y] == ' ') {
                for (char side : SIDES) {
                    vis.insert({x, y, side});
                }
                qadd({x + 1, y, 'u'});
                qadd({x - 1, y, 'd'});
                qadd({x, y + 1, 'l'});
                qadd({x, y - 1, 'r'});
            } else if (grid[x][y] == '/') {
                if (side == 'l' || side == 'u') {
                    vis.insert({x, y, 'l'});
                    vis.insert({x, y, 'u'});
                    qadd({x - 1, y, 'd'});
                    qadd({x, y - 1, 'r'});
                } else {
                    vis.insert({x, y, 'r'});
                    vis.insert({x, y, 'd'});
                    qadd({x + 1, y, 'u'});
                    qadd({x, y + 1, 'l'});
                }
            } else { // "\"
                if (side == 'l' || side == 'd') {
                    vis.insert({x, y, 'l'});
                    vis.insert({x, y, 'd'});
                    qadd({x + 1, y, 'u'});
                    qadd({x, y - 1, 'r'});
                } else {
                    vis.insert({x, y, 'r'});
                    vis.insert({x, y, 'u'});
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
        VisSet vis;
        for (int x = 0; x < grid.size(); ++x) {
            for (int y = 0; y < grid[0].size(); ++y) {
                for (char side : SIDES) {
                    if (!vis.contains({x, y, side})) {
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
