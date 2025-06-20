class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_ = 0
        MAX = 10 ** 5 + 2
        min_len = MAX
        for right in range(len(nums)):
            sum_ += nums[right]
            while sum_ >= target:
                min_len = min(min_len, right - left + 1)
                sum_ -= nums[left]
                left += 1
        return min_len if min_len != MAX else 0


        
