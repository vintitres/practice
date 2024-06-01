class Solution {
public:
    int scoreOfString(string s) {
        char last = s[0];
        int sum = 0;
        for (char c : s) {
            sum += abs(c - last);
            last = c;
        }
        return sum;
    }
};
