class Solution {
public:
    int countTriplets(vector<int>& arr) {
        int arrsize = arr.size();
        int triplets_cnt = 0;
        for (int i = 0; i < arrsize - 1; ++i) {
            int a = 0;
            for (int j = i + 1; j < arrsize; ++j) {
                a ^= arr[j - 1];
                int b = 0;
                for (int k = j; k < arrsize; ++k) {
                    b ^= arr[k];
                    if (a == b) {
                        ++triplets_cnt;
                    }
                }
            }
        }
        return triplets_cnt;
        
    }
};
