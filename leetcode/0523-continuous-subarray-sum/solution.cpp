class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int ns = nums.size();
        long long sum = 0;
        map<int, int> sum_counts;
        int sum_counts_next = 0;
        int ret = 0;
        for (int i = 0; i < ns; ++i) {
            sum += nums[i];
            sum %= k;
            int key = (k - sum) % k;
            auto it = sum_counts.find(key);
            if (it != sum_counts.end()) {
                ret += it->second;
            }
            int key2 = sum_counts_next;
            it = sum_counts.find(key2);
            if (it != sum_counts.end()) {
                ++(it->second);
            } else {
                sum_counts[key2] = 1;
            }
            sum_counts_next = key;
        }
        return ret;
    }
};
