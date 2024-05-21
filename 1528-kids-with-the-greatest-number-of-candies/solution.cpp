class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        
        int cs = candies.size();
        vector <bool> ret(cs);
        int mx = *max_element(candies.begin(), candies.end());
        for (int i =0; i < cs; ++i) {
            ret[i] = candies[i] + extraCandies >= mx;
        }
        return ret;
    }
};
