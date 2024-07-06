class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        short nsize = nums.size();
        int allsize = 1<<nsize;
        int beaut_sets = 0;
        map<int, set<short>> nums_seen;
        set<pair<short,short>> ugly_pairs_indicies;
        for (int i = 0; i < nsize; ++i) {
            int n = nums[i];
            auto it = nums_seen.find(n - k);
            if (it != nums_seen.end()) {
                nums_seen[n] = set<short>();
                for (auto j : it->second) {
                    ugly_pairs_indicies.insert(make_pair(j, i));
                }

            }
            nums_seen[n].insert(i);
        }
        for (int set_bitmask = 1; set_bitmask < allsize; ++set_bitmask) {
            bool ok = true;
            for (auto ugly_pair : ugly_pairs_indicies) {
                int i, j;
                tie(i, j) = ugly_pair;
                if (set_bitmask & 1<<i && set_bitmask & 1<<j) {
                    ok = false;
                    if (j > 0) {
                        //bitset<16> ii(i);
                        //bitset<16> iv(i + 1);
                        //cout << ii << " " << j << " " << iv << endl;
                        set_bitmask = set_bitmask | ((1<<i) - 1);
                        // 1010101......
                        // 0000001000000
                        //bitset<16> iii(i + 1);
                        //cout << iii << endl;
                    }
                    break;
                }
            }
            //bitset<4> m(set_bitmask);
            //cout << m;

            if (ok) {
                //cout << "!";
                beaut_sets++;
            }
            //cout << endl;
        }
        return beaut_sets;
    }
};
