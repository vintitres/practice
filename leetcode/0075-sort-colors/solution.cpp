class Solution {
    void sortColors(vector<int>& nums, int start, int end) {
        if (start + 1 == end) {
            return;
        }
        int mid = (end + start + 1) / 2;
        // cout << start << " " << end << " " << mid << endl;
        sortColors(nums, start, mid);
        sortColors(nums, mid, end);
        for (int i = start, j = mid; i < j && j < end;) {
            if (nums[i] <= nums[j]) {
                ++i;
            } else {
                // slow shift
                int last = nums[j];
                ++j;
                for (int k = i; k < j; ++k) {
                    swap(last, nums[k]);
                }
            }
        }
    }
public:
    void sortColors(vector<int>& nums) {
        sortColors(nums, 0, nums.size());
    }
};
