class Solution {
    bool is_pali(string& s, int start, int len) {
    for (int i = start, j = start + len - 1; i < j;) {
        cout << i << "=" << j << endl;
        if (s[i++] != s[j--]) {
            cout << "!" << endl; 
            return false;
        }
                             
    }
    cout << "pali" << endl;
    return true;
}
public:
    
    vector<vector<string>> partition(string &s, int start = 0) {
        cout << start << endl;
        vector<vector<string>> ret;
        int ssize = s.size();
        if (start == ssize) {
            vector<string> e;
            ret.push_back(e);
            return ret;
}
        
        
        for (int l = 1; l <= ssize - start; ++l) {
            cout << start << "?" << l << endl;
            if (is_pali(s, start, l)) {
                cout << start << " " << l << endl;
                for (auto p : partition(s, start + l)) {
                   auto np = p;
                    p.insert(p.begin(), s.substr(start, l));
                    ret.push_back(p);
}
}
            cout << start << "!" << l << endl;
}
        cout << start << "!" << endl;
        return ret;
    }
};
