class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int last = nums[0]-1;
        bool lasttwice = false;
        int j=0;
        for (int i = 0; i < nums.size(); ++i) {
if (last != nums[i] || !lasttwice){
lasttwice = last == nums[i];
    nums[j++] = nums[i];
last = nums[i];
} 
           
}
        
    
    return j;
    }
};
