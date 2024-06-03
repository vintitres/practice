class Solution {
public:
    int appendCharacters(string s, string t) {
        int foundchars = 0;
        int sindex = 0;
        for (char c: t) {
            while(sindex < s.size() && s[sindex] != c) {
                ++sindex;
            }
            if (sindex == s.size()) {
                break;
            }
            ++sindex;
            ++foundchars;
        } 
        return t.size() - foundchars;
    }
};
