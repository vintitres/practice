class Solution {
public:
    // if no nums then 1 2 4 8 16 ... n is best
    //
    // once I get 1,...,m and nothing beyond then i can double the range on each patch, so need log2(n / m) extra patches
    int minPatches(vector<int>& nums, int n) {
        int patches = 0;
        long long max_sum = 0;
        for (long long num : nums) {
            while (max_sum + 1 < num) {
                max_sum += max_sum + 1;
                // cout << max_sum + 1 << endl;
                ++patches;
                if (max_sum >= n) {
                    return patches;
                }
            }
            max_sum += num;
            // cout << num << "." << endl;
            if (max_sum >= n) {
                return patches;
            }
        }
        while (max_sum < n) {
            // cout << max_sum + 1 << endl;
            max_sum += max_sum + 1;
            ++patches;
        }
        return patches;
    }
};
