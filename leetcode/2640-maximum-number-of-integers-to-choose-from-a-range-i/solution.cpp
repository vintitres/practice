class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        sort(banned.begin(), banned.end());
        int sum = 0;
        auto banned_it = banned.begin();
        int count = 0;
        for (int i = 1; i <= n; ++i) {
            if (banned_it != banned.end() && *banned_it == i) {
                while (banned_it != banned.end() && *banned_it == i) {
                    ++banned_it;
                }
                continue;
            }
            sum += i;
            if (sum > maxSum) {
                break;
            }
            ++count;
        }
        return count;
    }
};
