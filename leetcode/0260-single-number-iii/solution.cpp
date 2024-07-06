class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int xorall = 0;
        for (int num: nums) {
            xorall ^= num;
        }
        int splitbit = 1;
        while (!(xorall & splitbit)) {
            splitbit <<= 1;
        }
        int xorA = 0, xorB = 0;
        for (int num: nums) {
            if (num & splitbit) {
                xorA ^= num;
            } else {
                xorB ^= num;
            }
        }

        return vector<int>({xorA, xorB});
        
    }
};
