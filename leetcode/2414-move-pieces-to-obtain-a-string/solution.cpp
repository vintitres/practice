class Solution {
public:
    bool canChange(string start, string target) {
        int sl = target.size();
        int tl = target.size();
        vector<pair<int, char>> startpos, targetpos;
        for (int i = 0; i < sl; ++i) {
            if (start[i] != '_') {
                startpos.push_back({i, start[i]});
            }
            if (target[i] != '_') {
                targetpos.push_back({i, target[i]});
            }
        }
        int startposl = startpos.size();
        if (startposl != targetpos.size()) {
            return false;
        }
        for (int i = 0; i < startposl; ++i) {
            if (startpos[i].second != targetpos[i].second) {
                return false;
            }
            if (startpos[i].second == 'R' && startpos[i].first > targetpos[i].first) {
                return false;
            }
            if (startpos[i].second == 'L' && startpos[i].first < targetpos[i].first) {
                return false;
            }
        }
        return true;
    }
};
