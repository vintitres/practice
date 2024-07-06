class Solution {
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        sort(arr2.begin(), arr2.end());
        int a1s = arr1.size(), a2s = arr2.size();
        int dp[a1s][2];
        for (int i = 0; i < a1s; ++i) {
            dp[i][0] = INT_MAX;
            dp[i][1] = INT_MAX;
        }
        for (int j = 0; j < a1s + 1; ++j) {
            int k = 0;
            int jj = j % 2;
            int jjj = (j + 1) % 2;
            for (int i = 0; i < a1s; ++i) {
                int prev = i > 0 ? dp[i - 1][jj] : -1;
                dp[i][jj] = arr1[i] > prev ? arr1[i] : INT_MAX;
                if (j > 0) {
                    if (dp[i][jjj] > prev) {
                        dp[i][jj] = min(dp[i][jj], dp[i][jjj]);
                    }
                    int r = a2s - 1;
                    int prev2 = (i > 0 ? dp[i - 1][jjj] : -1);
                    while (k <= r) {
                        int m = k + (r - k) / 2;
                        if (arr2[m] <= prev2) {
                            k = m + 1;
                        } else {
                            r = m - 1;
                        }
                    }
                    if (k < a2s) {
                        dp[i][jj] = min(dp[i][jj], arr2[k]);
                    }
                }
                if (dp[i][jj] == INT_MAX) {
                    break;
                }
            }
            if (dp[a1s - 1][jj] < INT_MAX) {
                return j;
            }
        }
        return -1;
    }
};
