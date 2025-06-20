class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum_ = 0
        length = len(nums)
        min_len = length
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
        if left == 0 and sum_ < target:
            return 0
        return min_len


        
