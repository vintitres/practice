class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> merged;
        for (int i = 0, j = 0; i <m || j < n;) {
if (j == n || (i < m && nums1[i] <= nums2[j])) {
        merged.push_back(nums1[i++]);
    } else {merged.push_back(nums2[j++]);}
        }
    nums1 = merged;
    }
};
