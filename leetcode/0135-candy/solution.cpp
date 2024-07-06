class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> candies(ratings.size(), 0);
        for (unsigned int i = 0; i < ratings.size(); ++i) {
            //cout << i <<endl;
            if (candies[i] != 0) continue;
            if ((i == 0 || ratings[i] <= ratings[i - 1]) && (i == ratings.size() - 1 || ratings[i] <= ratings[i + 1])) {
                candies[i] = 1;
                for (int j = i - 1; j >= 0; --j) {
                    //cout << "j1 " << j <<endl;
                    if (ratings[j] > ratings[j + 1]) {
                        candies[j] = max(candies[j], candies[j + 1] + 1);
                    } else {
                        break;
                    }
                }
                for (unsigned int j = i + 1; j < ratings.size(); ++j) {
                    
                    //cout << "j1 " << j <<endl;
                    if (ratings[j] > ratings[j - 1]) {
                        candies[j] = max(candies[j], candies[j - 1] + 1);
                    } else {
                        break;
                    }
                }
                
            }
        }
        int s = 0;
        for (int c: candies) {
            s += c;
        }
        return s;
    }
    // 1 0 2 2 3 0 3 4 5 1 1 0
    //   v ^ = ^ v ^ ^ ^ v = v
    // 1 0 1 0 1 0 1 2 3 0 0 -1
    // ^ v = v ^ v v v ^ = ^ 
    
    // v v -> 1
    // = = -> 1
    // v = -> 1
    // = v -> 1
    
    // ^ ^ -> max(l,r)
    // ^ (=/v) -> l + 1
    // (=/v) ^ -> r + 1
    
    
    
    // 9 5 8 7 6 5
    //   1
    
    // 
};
