class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int ssize = s.size();
        vector<int> costs;
        for (int i = 0; i < ssize; ++i) {
            costs.push_back(abs(s[i] - t[i]));
        }
        int max_len = 0;
        for (int b = 0, e = 0, sum = 0; e < ssize; ++e) {
            sum += costs[e];
            while (sum > maxCost) {
                sum -= costs[b++];
            }
            max_len = max(max_len, e - b + 1);
        }
        return max_len;
    }
};
