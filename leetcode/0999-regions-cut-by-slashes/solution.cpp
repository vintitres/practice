const char SIDES[] = {'l', 'r', 'u', 'd'};
typedef set<tuple<int, int, char>> VisSet;

class Solution {
    void fill_area(int x, int y, char side, vector<string> const& grid,
                   VisSet& vis) {
        if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size() ||
            vis.contains({x, y, side})) {
            return;
        }
        // cout << x << " " << y << " " << side << endl;
        if (grid[x][y] == ' ') {
            for (char side : SIDES) {
                vis.insert({x, y, side});
            }
            fill_area(x + 1, y, 'u', grid, vis);
            fill_area(x - 1, y, 'd', grid, vis);
            fill_area(x, y + 1, 'l', grid, vis);
            fill_area(x, y - 1, 'r', grid, vis);
        } else if (grid[x][y] == '/') {
            if (side == 'l' || side == 'u') {
                vis.insert({x, y, 'l'});
                vis.insert({x, y, 'u'});
                fill_area(x - 1, y, 'd', grid, vis);
                fill_area(x, y - 1, 'r', grid, vis);
            } else {
                vis.insert({x, y, 'r'});
                vis.insert({x, y, 'd'});
                fill_area(x + 1, y, 'u', grid, vis);
                fill_area(x, y + 1, 'l', grid, vis);
            }
        } else { // "\"
            if (side == 'l' || side == 'd') {
                vis.insert({x, y, 'l'});
                vis.insert({x, y, 'd'});
                fill_area(x + 1, y, 'u', grid, vis);
                fill_area(x, y - 1, 'r', grid, vis);
            } else {
                vis.insert({x, y, 'r'});
                vis.insert({x, y, 'u'});
                fill_area(x - 1, y, 'd', grid, vis);
                fill_area(x, y + 1, 'l', grid, vis);
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
