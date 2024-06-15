class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int size = profits.size();
        vector<pair<int,int>> capital_profits(size);
        for (int i = 0; i < size; ++i) {
            capital_profits[i] = make_pair(capital[i], profits[i]);
        }
        sort(capital_profits.begin(), capital_profits.end());
        multiset<int> available_profits;
        int capital_profits_index = 0;
        for (int i = 0; i < k; ++i) {
            for (; capital_profits_index < size; ++capital_profits_index) {
                auto cp = capital_profits[capital_profits_index];
                if (cp.first <= w) {
                    available_profits.insert(-cp.second);
                } else {
                    break;
                }
            }
            if (available_profits.empty()) {
                break;
            }
            auto it = available_profits.begin();
            w += -*it;
            available_profits.erase(it);
        }
        return w;
    }
};
