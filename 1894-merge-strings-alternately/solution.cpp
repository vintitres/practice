class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        unsigned int size1 = word1.size(),  size2 = word2.size();
        unsigned int sizemax = max(size1, size2);
        string merged;
        for (unsigned int i = 0; i < sizemax; ++i) {
if (i < size1){merged += word1[i];}
            if (i < size2){merged += word2[i];}
}
        return merged;
        
    }
};
