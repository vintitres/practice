class Solution {
public:
    void reverse(vector<int>& nums, unsigned int start, unsigned int end) {
        for (unsigned int i = start, j = end -1; i < j;) {
            swap(nums[i++], nums[j--]);
        }
    }
    void rotate(vector<int>& nums, int k) {
        unsigned int nums_size = nums.size();
        k = k % nums_size;
        if (k == 0) return;
        reverse(nums, 0, nums_size);
        reverse(nums, 0, k);
        reverse(nums, k, nums_size);   
    }
};
