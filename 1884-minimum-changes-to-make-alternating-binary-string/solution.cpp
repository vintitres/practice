class Solution {
public:
    int minOperations(string s) {
        short c1 = 0, c2 = 0, ssize = s.size();
        for (short i = 0; i < ssize; ++i) {
            if (i % 2 != s[i] - '0') {
                ++c1;
            } else {
                ++c2;
            }
        }
        return c1 < c2 ? c1 : c2;
    }
};
