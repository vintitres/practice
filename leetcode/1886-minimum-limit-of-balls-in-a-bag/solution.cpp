class Solution {
    bool canDo(vector<int> const& nums, int maxOperations, int penalty) {
        int op = 0;
        for (int num : nums) {
            op += num / penalty;
            if (num % penalty == 0) {
                op -= 1;
            }
            if (op > maxOperations) {
                return false;
            }
        }
        return true;
    }
public:
    int minimumSize(vector<int>& nums, int maxOperations) {
        int b = 1, e = 1000000001;
        while (b < e) {
            int m = (e + b) / 2;
            if (canDo(nums, maxOperations, m)) {
                e = m;
            } else {
                b = m + 1;
            }
        }
        return e;
    }
};
