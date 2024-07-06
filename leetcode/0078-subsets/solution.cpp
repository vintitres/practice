class Solution {
    void subsets_add(vector<vector<int>>& subsets, int x) {
        
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> empty;
        vector<vector<int>> subsets;
        subsets.push_back(empty);
        for (int n: nums) {
            int size = subsets.size();
            for (int i = 0; i < size; ++i) {
                vector<int> newsubset(subsets[i]);
                newsubset.push_back(n);
                subsets.push_back(newsubset);
            }
        }
        return subsets;
    }
};

/*

[] [1] [2] [1, 2] + 3
[3] [1, 3] [2, 3] [1, 2]
*/
