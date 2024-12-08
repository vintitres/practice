class Solution {
    struct Event {
        int start;
        int end;
        int value;
    };
    tuple<int, int, int> event(vector<int> &e) {
        return make_tuple(e[0], e[1], e[2]);
    }
public:
    int maxTwoEvents(vector<vector<int>>& events) {
        vector<tuple<int, int, int>> evs;
        for (auto ev : events) {
            evs.push_back(event(ev));
        }
        sort(evs.begin(), evs.end());
        map<int, int> max_after;
        int mx = 0;
        for (int i = evs.size() - 1; i >= 0; --i) {
            mx = max(mx, get<2>(evs[i]));
            int start = get<0>(evs[i]);
            max_after[start] = mx;
        }
        mx = 0;
        for (auto ev : evs) {
            int end = get<1>(ev);
            int val = get<2>(ev);
            auto it = max_after.upper_bound(end);
            if (it != max_after.end()) {
                val += it->second;
            }
            mx = max(mx, val);
        }
        return mx;
    }
};
