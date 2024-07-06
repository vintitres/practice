class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        map<int,int> num_to_pos;
        int arr2s = arr2.size();
        for (int i = 0; i < arr2s; ++i) {
            num_to_pos[arr2[i]] = i;
        }
        auto cmp = [&num_to_pos](int a, int b) {
            auto ita = num_to_pos.find(a);
            auto itb = num_to_pos.find(b);
            if (ita == num_to_pos.end()) {
                if (itb == num_to_pos.end()) {
                    return a < b;
                }
                return false;

            }
            if (itb == num_to_pos.end()) {
                return true;
            }
            return ita->second < itb->second;
        };
        auto arr = arr1;
        sort(arr.begin(), arr.end(), cmp);
        return arr;
        
    }
};
