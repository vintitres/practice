class Solution {
    bool check(string s, unsigned int l, string s2 = "") {
        if (s.size() < l) return false;
        string sdiv = s2 == "" ? s.substr(0, l) : s2.substr(0,l) ;
for (int i = 0; i < s.size() / l; ++i) {
if (s.substr(i * l, l) != sdiv) return false;
}
        return true;
}
public:
    string gcdOfStrings(string str1, string str2) {
        
        for (int i = 1; i <= str1.size(); ++i) {
if (str1.size() % i == 0 && str2.size() % (str1.size() / i) == 0 && check(str1, str1.size() / i) &&
check(str2, str1.size() / i, str1)){
return str1.substr(0, str1.size() /i);
}
}
    return "";
        
    }
};
