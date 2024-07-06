class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int numssize = nums.size();
        int size = numssize;
        for (int i = 0; i < size; ++i) {
            while (i < size && nums[i] == val) {
                swap(nums[i], nums[(size--) - 1]);
            }
        }
        return size;
    }
};
