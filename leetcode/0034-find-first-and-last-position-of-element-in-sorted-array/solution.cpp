class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ret({-1,-1});
        if (nums.size() == 0) return ret;
        int b = 0, e = nums.size() - 1;
        while (b < e) {
            int m = (b + e) / 2;
            if (nums[m] < target) {
                b = m + 1;
            } else {
                e = m;
            }
        }
        if (b <0 || nums[b] != target) return ret;
        ret[0] = b;
        b = 0;
        e = nums.size() - 1;
        while (b < e) {
            int m = (b + e + 1) / 2;
            if (nums[m] <= target) {
                b = m;
            } else {
                e = m - 1;
            }
        }
        ret[1] = e;
        return ret;
    }
};
