class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        ret = 0
        while i < j:
            x = k - nums[i]
            while i < j and nums[j] > x:
                j -= 1
            if i < j and nums[j] == x:
                j -= 1
                ret += 1
            i += 1
        return ret
        
