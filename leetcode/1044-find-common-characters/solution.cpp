class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        int char_count[26];
        for (int i = 0; i < 26; ++i) {
            char_count[i] = 0;
        }
        for (char c : words[0]) {
            ++char_count[c - 'a'];
        }
        for (string word : words) {
            int char_count_word[26];
            for (int i = 0; i < 26; ++i) {
                char_count_word[i] = 0;
            }
            for (char c : word) {
                ++char_count_word[c - 'a'];
            }
            for (int i = 0; i < 26; ++i) {
                char_count[i] = min(char_count[i], char_count_word[i]);
            }
        }
        vector<string> chars;
        for (int i = 0; i < 26; ++i) {
            string s;
            s += 'a' + i;
            for (int j = 0; j < char_count[i]; ++j) {
                chars.push_back(s);
            }
        }
        return chars;
    }
};
