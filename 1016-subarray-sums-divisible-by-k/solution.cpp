class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int numss = nums.size();
        int sum = 0;
        int count = 0;
        vector<int> sums_count(k, 0);
        sums_count[0] = 1;
        for (int i = 0; i < numss; ++i) {
            sum += nums[i];
            sum %= k;
            count += sums_count[(k - sum) % k];
            ++sums_count[(k - sum) % k];
        }
        return count;
    }
};
