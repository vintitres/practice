class Solution {
public:
    int numDecodings(string s) {
        int ssize = s.size();
        vector<int> num_decodings(ssize, 0);
        num_decodings[ssize - 1] = s[ssize - 1] == '0' ? 0 : 1;
        for (int i = ssize - 2; i >= 0; --i) {
            if (s[i] != '0') {
                num_decodings[i] = num_decodings[i + 1];
            }
            if (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6')) {
                num_decodings[i] += (i + 2 == ssize) ? 1 : num_decodings[i + 2];
            }
        }
        return num_decodings[0];

        
    }
};
