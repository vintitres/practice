class Solution {
public:
    int jump(vector<int>& nums) {
        int nums_size = nums.size();
        vector<int> jumps_needed(nums_size, nums_size + 1);
        jumps_needed[0] = 0;
        for (int i = 0; i < nums_size; ++i) {
            for (int j = 0; j < nums_size && j <= i + nums[i]; ++j) {
                jumps_needed[j] = min(jumps_needed[j], jumps_needed[i] + 1);
            }
        }   
        return jumps_needed[nums.size() - 1];
        
    }
};
