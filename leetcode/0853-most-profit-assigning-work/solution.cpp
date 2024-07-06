class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        int ds = difficulty.size();
        vector<pair<int,int>> difficulty_profit(ds);
        for (int i = 0; i < ds; ++i) {
            difficulty_profit[i] = make_pair(difficulty[i], profit[i]);
        }
        sort(difficulty_profit.begin(), difficulty_profit.end());/*, [](pair<int,int> a, pair<int, int> b){
            if (a.first == b.first) {
                return a.second > b.second;
            }
            return a.first < b.first;
        });
        for (auto dp : difficulty_profit) {
            cout<< dp.first << " " << dp.second << endl;
        }
        */
        sort(worker.begin(), worker.end());
        int ws = worker.size();
        int prof = 0;
        int max_prof = 0;
        for (int di = -1, wi = 0; wi < ws; ++wi) {
            while (di + 1 < ds && difficulty_profit[di + 1].first <= worker[wi]) {
                ++di;
                max_prof = max(max_prof, difficulty_profit[di].second);
            }
            prof += max_prof;

        }
        return prof;
    }
};
