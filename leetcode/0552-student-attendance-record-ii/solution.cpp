class Solution {
    const int MOD = 1000000007;
public:
    int checkRecord(int n) {
        int mem[2][2][3];
        for (int a = 0; a < 2; ++a) {
            for (int l = 0; l < 3; ++l) {
                mem[0][a][l] = 1;
            }
        }

        for (int i = 1; i <= n; ++i) {
            for (int a = 0; a < 2; ++a) {
                for (int l = 0; l < 3; ++l) {
                    int curi = i % 2;
                    int lasti = (i + 1) % 2;
                    int x = mem[lasti][a][0];
                    x %= MOD;
                    if (a < 1) {
                        x += mem[lasti][a + 1][0];
                        x %= MOD;
                    }
                    if (l < 2) {
                        x += mem[lasti][a][l + 1];
                        x %= MOD;
                    }
                    mem[curi][a][l] = x;
                }
            }
        }
        return mem[n % 2][0][0];
    }
};
