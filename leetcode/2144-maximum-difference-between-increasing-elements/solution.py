class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_in_suffix = [0] * len(nums)
        mx = 0
        for i in reversed(range(0, len(nums))):
            mx = max(mx, nums[i])
            max_in_suffix[i] = mx
        mx_diff = -1
        for i in range(0, len(nums) - 1):
            diff = max_in_suffix[i + 1] - nums[i]
            if diff > 0:
                mx_diff = max(mx_diff, diff)
        return mx_diff
        
        
