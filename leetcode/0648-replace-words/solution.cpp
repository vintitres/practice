class Solution {
    string root(string word, set<string>& dictionary) {
        for (int len = 1; len < word.size(); ++len) {
            string root = word.substr(0, len);
            if (dictionary.contains(root)) {
                return root;
            }
        }
        return word;
    }
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        set<string> dictionary_set(dictionary.begin(), dictionary.end());
        string new_sentence;
        stringstream ss(sentence);
        string word;
        while (ss >> word) {
            new_sentence += root(word, dictionary_set) + " ";
        }
        return new_sentence.substr(0, new_sentence.size() - 1);
    }
};

