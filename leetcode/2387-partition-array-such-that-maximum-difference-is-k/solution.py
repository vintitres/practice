class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        nums = sorted(nums)
        last_start = nums[0]
        subsqs = 1
        for num in nums:
            if num > last_start + k:
                subsqs += 1
                last_start = num
        return subsqs

        
