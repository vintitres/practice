class Solution {
public:
    int longestPalindrome(string s) {
        vector<bool> seenchar(52, false);
        int pairs = 0;
        int singles = 0;
        for (char c : s) {
            short charindex = c <= 'Z' ? c - 'A' : c - 'a' + 26;
            if (seenchar[charindex]) {
                ++pairs;
                seenchar[charindex] = false;
                --singles;
            } else {
                seenchar[charindex] = true;
                ++singles;
            }
        }
        return pairs * 2 + (singles > 0 ? 1 : 0);
        
    }
};
