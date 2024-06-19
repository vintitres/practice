class Solution {
public:
    bool canBouquet(vector<int>& bloomDay, int m, int k, int day) {
        int kk = k;
        //cout << day << endl;
        for (int bloom_day : bloomDay) {
            if (day >= bloom_day) {
                //cout << bloom_day << "ok" <<endl;
                //cout << m << " " << kk <<endl;
                --kk;
                if (kk == 0) {
                    kk = k;
                    --m;
                    if (m == 0) {
                        return true;
                    }
                } 
            } else {
                //cout << bloom_day << "no" <<endl;
                kk = k;
            }
        }
        return false;
    }
    int minDays(vector<int>& bloomDay, int m, int k) {
        int mx = 0;
        for (int bloom_day : bloomDay) {
            mx = max(mx, bloom_day);
        }
        int b = 0, e = mx + 1;
        while (b < e) {
            int mi = (b + e) / 2;
            if (canBouquet(bloomDay, m, k, mi)) {
                e = mi;
            } else {
                b = mi + 1;
            }
        }
        return b == mx + 1 ? -1 : b;
    }
};
