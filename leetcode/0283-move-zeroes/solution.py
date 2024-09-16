class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes_start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if zeroes_start < i:
                    nums[zeroes_start] = nums[i]
                    nums[i] = 0
                zeroes_start = zeroes_start + 1

        
