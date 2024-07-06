class Solution {
public:
    int findGCD(vector<int>& nums) {
        
        int mx = nums[0], mi = nums[0];
        for (int n : nums) {
            if (n > mx)mx =n;
            else if (n < mi)mi = n;
}
        return gcd(mx, mi);
    }
};
