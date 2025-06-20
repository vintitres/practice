class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum_ = 0
        length = len(nums)
        min_len = length + 1
        while right <= length:
            if sum_ < target:
                if right == length:
                    break
                sum_ += nums[right]
                right += 1
            else:
                min_len = min(min_len, right - left)
                sum_ -= nums[left]
                left += 1
        if min_len == length + 1:
            return 0
        return min_len


        
