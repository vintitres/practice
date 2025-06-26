class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = dict((num, i) for i, num in enumerate(nums))
        for i, num in enumerate(nums):
            if target - num in nums_set:
                j = nums_set[target - num]
                if i == j:
                    continue
                return (i, j)

            
        
