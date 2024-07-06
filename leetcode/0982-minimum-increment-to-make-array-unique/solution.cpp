class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int min = -1;
        int inc = 0;
        for (int num : nums) {
            if (num > min) {
                min = num;
            } else {
                inc += min + 1 - num;
                ++min;
            }
        }
        return inc;
        
    }
};
