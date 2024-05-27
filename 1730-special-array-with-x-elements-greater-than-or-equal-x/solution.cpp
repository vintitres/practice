class Solution {
public:
    int specialArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            // 3 9 7 8 3 8 6 6
            // 3 3 6 6 7 8 8 9
            // 0 1 2 3 4 5 6 7
            // 8 7 6 5 4 3 2 1
            // 
            int x = nums.size() - i;
            if (nums[i] >= x && (i == 0  || nums[i - 1] < x)) {
                return x;
            }
        }
        return -1;
        
    }
};
