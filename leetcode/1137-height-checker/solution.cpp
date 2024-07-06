class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> expected(heights.begin(), heights.end());
        sort(expected.begin(), expected.end());
        int diff = 0;
        int hs = heights.size();
        for (int i = 0; i < hs; ++i) {
            if (expected[i] != heights[i]) {
                ++diff;
            }
        }
        return diff;
        
    }
};
