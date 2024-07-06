class Solution {
public:
    int numSteps(string s) {
        /*
        1 0001 0010
        2 0010 0001
        3 0011 0100
        4 0100 0010 
        5 0101 0110
        6 0110 0011
        7 0111 1000
        8 1000 0100
        9 1001
       10 1010
       11 1011
       12 1100
       13 1101 1110 
       14 1110 0111
       15
        */
        //cout << s << endl;
        int ssize = s.size();
        if (s[ssize - 1] == '1') {
            if (ssize == 1) return 0; 
            bool done = false;
            for (int i = ssize - 1; i >= 0; --i) {
                if (s[i] == '0') {
                    s[i] = '1';
                    done = true;
                    break;
                }
                s[i] = '0';
            }
            if (!done) {
                s = "1" + s;
            }
        } else {
            s.resize(s.size() - 1);
        }
        return 1 + numSteps(s);
        
    }
};
