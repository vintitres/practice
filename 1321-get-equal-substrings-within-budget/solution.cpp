class Solution {
public:
    int cost(char x, char y) {
        return (int)(x < y ? y - x : x - y);
    }
    int equalSubstring(string s, string t, int maxCost) {
        int begin = 0, end = 0, currCost = 0, maxLen = 0, ss = s.size();
        while (end < ss) {
            currCost += cost(s[end], t[end]);
            ++end;
            while (currCost > maxCost) {
                currCost -= cost(s[begin], t[begin]);
                ++begin;
            }
            maxLen = max(maxLen, end - begin);
        }
        return maxLen;
    }
};
