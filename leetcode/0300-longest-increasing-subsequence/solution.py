class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest = [1] * len(nums)
        for i, num in enumerate(nums):
            longest[i] = max(longest[j] if num > nums[j] else 0 for j in range(i)or [0]) + 1
        return max(longest)

        
